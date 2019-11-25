# -*- coding: utf-8 -*- 
# @Time : 2019/11/25 上午9:55 
# @Author : yangchengkai
# @File : Scheduler.py
import os
import json
import logging
from os.path import join, exists

from scrapy.utils.reqser import request_to_dict, request_from_dict
from scrapy.utils.misc import load_object
from scrapy.utils.job import job_dir

logger = logging.getLogger(__name__)


class Scheduler(object):

    def __init__(self, dupefilter, jobdir=None, dqclass=None, mqclass=None,
                 logunser=False, stats=None, pqclass=None):
        """
        实例化
        :param dupefilter: 链接去重器
        :param jobdir:磁盘队列的工作目录
        :param dqclass: 磁盘队列类名
        :param mqclass: 内存队列类名
        :param logunser: 是否记录日志请求
        :param stats:
        :param pqclass: 优先队列类名
        """
        self.df = dupefilter
        self.dqdir = self._dqdir(jobdir)
        self.pqclass = pqclass
        self.dqclass = dqclass
        self.mqclass = mqclass
        self.logunser = logunser
        self.stats = stats

    @classmethod
    def from_crawler(cls, crawler):
        """
        类方法，按照配置文件settings中的配置项，生成调度器实例。
        :param crawler: 爬虫类
        :return: 实例化调度器（调用__init__方法）
        """
        settings = crawler.settings
        # 链接去重器 scrapy.dupefilters.RFPDupeFilter
        dupefilter_cls = load_object(settings['DUPEFILTER_CLASS'])
        dupefilter = dupefilter_cls.from_settings(settings)
        # 优先队列类 queuelib.PriorityQueue
        pqclass = load_object(settings['SCHEDULER_PRIORITY_QUEUE'])
        # 磁盘队列类 scrapy.squeues.PickleLifoDiskQueue
        dqclass = load_object(settings['SCHEDULER_DISK_QUEUE'])
        # 内存队列类 scrapy.squeues.LifoMemoryQueue
        mqclass = load_object(settings['SCHEDULER_MEMORY_QUEUE'])
        # 日志
        logunser = settings.getbool('LOG_UNSERIALIZABLE_REQUESTS', settings.getbool('SCHEDULER_DEBUG'))
        return cls(dupefilter, jobdir=job_dir(settings), logunser=logunser,
                   stats=crawler.stats, pqclass=pqclass, dqclass=dqclass, mqclass=mqclass)

    def has_pending_requests(self):
        """
        判断调度器中是否为空
        :return: 是否还有链接
        """
        return len(self) > 0

    def open(self, spider):
        """
        实例化内存队列、磁盘队列、链接去重器
        :param spider: 自定义爬虫
        :return: 链接去重器是否开启成功
        """
        self.spider = spider
        # 优先内存队列实例
        self.mqs = self.pqclass(self._newmq)
        # 优先磁盘队列实例，如果在启动时候设置了JOBDIR，则激活磁盘队列实例，否则设置为None,
        self.dqs = self._dq() if self.dqdir else None
        # 链接去重器
        return self.df.open()

    def close(self, reason):
        """
        关闭磁盘队列
        :param reason: 关闭原因
        :return: 链接去重器是否关闭成功
        """
        if self.dqs:
            prios = self.dqs.close()
            with open(join(self.dqdir, 'active.json'), 'w') as f:
                json.dump(prios, f)
        return self.df.close(reason)

    def enqueue_request(self, request):
        """
        请求入队列
        :param request:请求
        :return: True
        """
        # 如果请求需要去重，并且链接去重器中见过该请求，那么不需要进请求
        if not request.dont_filter and self.df.request_seen(request):
            self.df.log(request, self.spider)
            return False
        # 磁盘优先队列去重
        dqok = self._dqpush(request)
        # 如果是，则记录日志
        if dqok:
            self.stats.inc_value('scheduler/enqueued/disk', spider=self.spider)
        # 如果否，则用内存优先队列去重
        else:
            self._mqpush(request)
            self.stats.inc_value('scheduler/enqueued/memory', spider=self.spider)
        self.stats.inc_value('scheduler/enqueued', spider=self.spider)
        return True

    def next_request(self):
        """
        出队列
        :return:请求
        """
        # 从内存优先队列取
        request = self.mqs.pop()
        # 如果有结果，记录日志
        if request:
            self.stats.inc_value('scheduler/dequeued/memory', spider=self.spider)
        # 否则从磁盘队列取。
        else:
            request = self._dqpop()
            if request:
                self.stats.inc_value('scheduler/dequeued/disk', spider=self.spider)
        if request:
            self.stats.inc_value('scheduler/dequeued', spider=self.spider)
        return request

    def __len__(self):
        return len(self.dqs) + len(self.mqs) if self.dqs else len(self.mqs)

    def _dqpush(self, request):
        """
        :param request:
        :return:是否需要磁盘队列去重
        """
        if self.dqs is None:
            return
        try:
            reqd = request_to_dict(request, self.spider)
            self.dqs.push(reqd, -request.priority)
        except ValueError as e:  # non serializable request
            if self.logunser:
                msg = ("Unable to serialize request: %(request)s - reason:"
                       " %(reason)s - no more unserializable requests will be"
                       " logged (stats being collected)")
                logger.warning(msg, {'request': request, 'reason': e},
                               exc_info=True, extra={'spider': self.spider})
                self.logunser = False
            self.stats.inc_value('scheduler/unserializable',
                                 spider=self.spider)
            return
        else:
            return True

    def _mqpush(self, request):
        """
        磁盘优先队列push
        :param request:
        :return:
        """
        self.mqs.push(request, -request.priority)

    def _dqpop(self):
        if self.dqs:
            d = self.dqs.pop()
            if d:
                return request_from_dict(d, self.spider)

    def _newmq(self, priority):
        # 返回内存队列实例
        return self.mqclass()

    def _newdq(self, priority):
        # 返回磁盘队列实例
        return self.dqclass(join(self.dqdir, 'p%s' % priority))

    def _dq(self):
        # 恢复上次的队列
        activef = join(self.dqdir, 'active.json')
        if exists(activef):
            with open(activef) as f:
                prios = json.load(f)
        else:
            prios = ()
        # 使用磁盘队列作为优先队列
        q = self.pqclass(self._newdq, startprios=prios)
        if q:
            logger.info("Resuming crawl (%(queuesize)d requests scheduled)",
                        {'queuesize': len(q)}, extra={'spider': self.spider})
        return q

    def _dqdir(self, jobdir):
        if jobdir:
            dqdir = join(jobdir, 'requests.queue')
            if not exists(dqdir):
                os.makedirs(dqdir)
            return dqdir
