# encoding=utf8
from types import GeneratorType

from twisted.internet import defer
from twisted.web.client import getPage
from twisted.internet import reactor
from queue import Queue
class Request(object):
    def __init__(self,url,callback):
        self.url = url
        self.callback = callback


class HttpResponse(object):
    def __init__(self,content,request):
        self.content = content
        self.request = request

class Scheduler(object):
    """
    任务调度器
    """
    def __init__(self):
        self.q = Queue()

    def open(self):
        pass
    def next_request(self):
        try:
            ret =  self.q.get(block=False)
        except Exception as e:
            ret = None
        return ret
        pass
    def enqueue_request(self,req):
        self.q.put(req)
        pass
    def size(self):
        return self.q.qsize()
class ExecutionEngine(object):
    """
    引擎：所有调度
    """
    def __init__(self):
        self._close = None
        self.scheduler = None
        self.max = 5
        self.crawlling = []
    def get_response_callback(self,content,request):
        self.crawlling.remove(request)
        response = HttpResponse(content,request)
        result = request.callback(response)
        import types
        if isinstance(result,GeneratorType):
            for req in result:
                self.scheduler.enqueue_request(req)
    def _next_request(self):
        if self.scheduler.size() == 0 and len(self.crawlling) == 0:
            self._close.callback(None)
            return

        while len(self.crawlling)<self.max:
            req = self.scheduler.next_request()
            if req is None:
                return
            self.crawlling.append(req)
            d = getPage(req.url.encode('utf-8'))
            d.addCallback(self.get_response_callback,req)
            d.addCallback(lambda _:reactor.callLater(0,self._next_request))
        pass
    @defer.inlineCallbacks
    def open_spider(self,start_requests):
        self.scheduler = Scheduler()
        yield self.scheduler.open()

        while True:
            try:
                req = next(start_requests)
            except StopIteration:
                break
            self.scheduler.enqueue_request(req)
        reactor.callLater(0,self._next_request)
        # pass
        # self._close = defer.Deferred()
        # yield self._close
    @defer.inlineCallbacks
    def start(self):
        self._close = defer.Deferred()
        yield self._close
    pass
class Crawler(object):
    """
    用于创建Scheduler与ExecutionEngine
    """
    def _create_engine(self):
        return ExecutionEngine()
    def _create_spider(self,spider_cls_path):
        # 分割出路径名和类名
        module_path,cls_name = spider_cls_path.rsplit(".",maxsplit=1)
        # 导入文件
        import importlib
        m = importlib.import_module(module_path)
        # 获得模块的属性，类名
        cls = getattr(m,cls_name)
        # 初始化类
        return cls()
    @defer.inlineCallbacks
    def crawl(self,spider_cls_path):
        engine = self._create_engine()
        spider = self._create_spider(spider_cls_path)
        # 由于start_requests中与yield关键字，因此是一个生成器。
        # 所以使用iter关键字让他生成迭代器
        start_requests = iter(spider.start_requests())
        yield engine.open_spider(start_requests)
        yield engine.start()
        pass

class CrawlerProcess(object):
    """
    defer 用于开启事件循环
    """
    def __init__(self):
        self._active = set()
    def crawl(self,spider_cls_path):
        """
        创建多个defer对象
        :return:
        """
        crawler = Crawler()
        d = crawler.crawl(spider_cls_path)
        self._active.add(d)
        pass

    def start(self):
        dd = defer.DeferredList(self._active)
        dd.addBoth(lambda _:reactor.stop())
        reactor.run()
        pass

class Command(object):

    def run(self):
        crawlerProcess = CrawlerProcess()

        spider_cls_path_list = [
            # "spider.chouti.ChoutiSpider",
            "spider.cnblogs.CnblogsSpider"
        ]

        for spider_cls_path in spider_cls_path_list:
            crawlerProcess.crawl(spider_cls_path)
        crawlerProcess.start()
        pass
if __name__ == "__main__":
    cmd = Command()
    cmd.run()