# -*- coding: utf-8 -*- 
# @Time : 2019/11/26 上午8:19 
# @Author : yangchengkai
# @File : dupefilters.py
from __future__ import print_function
import os
import logging

from scrapy.utils.job import job_dir
from scrapy.utils.request import request_fingerprint


class BaseDupeFilter(object):

    @classmethod
    def from_settings(cls, settings):
        return cls()

    def request_seen(self, request):
        return False

    def open(self):  # can return deferred
        pass

    def close(self, reason):  # can return a deferred
        pass

    def log(self, request, spider):  # log that a request has been filtered
        pass


class RFPDupeFilter(BaseDupeFilter):
    """Request Fingerprint duplicates filter"""

    def __init__(self, path=None, debug=False):
        """
        初始化请求指纹集合，并恢复JOBDIR中的指纹集合。
        :param path: JOBDIR，在爬虫启动时候设置。
        :param debug: 是否开启debug模式
        """
        # 指纹文件
        self.file = None
        # 指纹集合
        self.fingerprints = set()
        # 日志相关
        self.logdupes = True
        self.debug = debug
        self.logger = logging.getLogger(__name__)
        # 如果JOBDIR有效，则打开上次运行的指纹文件
        if path:
            self.file = open(os.path.join(path, 'requests.seen'), 'a+')
            self.file.seek(0)
            # 将文件中的指纹恢复到指纹集合self.fingerprints中
            self.fingerprints.update(x.rstrip() for x in self.file)

    @classmethod
    def from_settings(cls, settings):
        """
        获得爬虫中的两个参数：JOBDIR缓存磁盘目录，和DUPEFILTER_DEBUG是否开启debug模式
        :param settings: 爬虫配置
        :return: 调用__init__方法，获得实例
        """
        debug = settings.getbool('DUPEFILTER_DEBUG')
        return cls(job_dir(settings), debug)

    def request_seen(self, request):
        """
        判断请求指纹是否重复
        :param request: 请求
        :return: Boolean
        """
        # 将请求转换为请求指纹
        fp = self.request_fingerprint(request)
        # 如果出现在集合中则重复
        if fp in self.fingerprints:
            return True
        # 否则集合添加该指纹
        self.fingerprints.add(fp)
        # 如果指定了磁盘缓存，则写入该指纹到文件
        if self.file:
            self.file.write(fp + os.linesep)

    def request_fingerprint(self, request):
        return request_fingerprint(request)

    def close(self, reason):
        """
        关闭指纹文件句柄
        :param reason:
        :return:
        """
        if self.file:
            self.file.close()

    def log(self, request, spider):
        if self.debug:
            msg = "Filtered duplicate request: %(request)s"
            self.logger.debug(msg, {'request': request}, extra={'spider': spider})
        elif self.logdupes:
            msg = ("Filtered duplicate request: %(request)s"
                   " - no more duplicates will be shown"
                   " (see DUPEFILTER_DEBUG to show all duplicates)")
            self.logger.debug(msg, {'request': request}, extra={'spider': spider})
            self.logdupes = False

        spider.crawler.stats.inc_value('dupefilter/filtered', spider=spider)
