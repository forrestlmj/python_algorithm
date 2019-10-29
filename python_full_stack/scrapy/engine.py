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
        # 调度器就是个队列存储
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
        """
        放入队列中
        :param req:
        :return:
        """
        self.q.put(req)
        pass
    def size(self):
        return self.q.qsize()
class ExecutionEngine(object):
    """
    引擎：所有调度
    """
    def __init__(self):
        """
        引擎中有调度器与，正在抓取的队列（控制并发用）crawlling
        """
        self._close = None
        self.scheduler = None
        self.max = 5
        self.crawlling = []
    def get_response_callback(self,content,request):
        #　下载成功就将crawling中移除该请求
        self.crawlling.remove(request)
        # 实例化请求
        response = HttpResponse(content,request)
        # 调用request的callback也就是spider类的parse方法进行解析，返回一个生成器
        result = request.callback(response)
        import types
        #　如果是生成器，那就是request对象而不是item。
        if isinstance(result,GeneratorType):
            for req in result:
                # 将请求再次放入到调度器中
                self.scheduler.enqueue_request(req)
    def _next_request(self):
        # 如果调度器和队列中都没有请求说明抓取完成
        if self.scheduler.size() == 0 and len(self.crawlling) == 0:
            self._close.callback(None)
            return
        # 然后处理crawlling中的请求，只要小于并发数，就将请求放入到队列中
        while len(self.crawlling)<self.max:
            #　获得调度器中的请求
            req = self.scheduler.next_request()
            # 如果调度器中暂时没有请求，则退出　
            if req is None:
                return
            # 将请求放入正在抓取的crawlling中
            self.crawlling.append(req)
            # 下载请求
            d = getPage(req.url.encode('utf-8'))
            # 解析下载，将请求放入到解析函数中
            d.addCallback(self.get_response_callback,req)
            # 同时循环该方法
            d.addCallback(lambda _:reactor.callLater(0,self._next_request))
        pass
    @defer.inlineCallbacks
    def open_spider(self,start_requests):
        # 每次激活一个爬虫都分配一个调度器
        self.scheduler = Scheduler()
        # 调度器激活
        yield self.scheduler.open()
        # 迭代start_requests迭代器，next迭代器，将request放入到调度器中
        while True:
            try:
                req = next(start_requests)
            except StopIteration:
                break
            self.scheduler.enqueue_request(req)
        # 调度下一个请求
        reactor.callLater(0,self._next_request)
        # pass
        # self._close = defer.Deferred()
        # yield self._close
    @defer.inlineCallbacks
    def start(self):
        #　开始
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
        # 分割出路径名和类名,用于加载
        module_path,cls_name = spider_cls_path.rsplit(".",maxsplit=1)
        # 导入文件
        import importlib
        m = importlib.import_module(module_path)
        # 获得模块的属性，爬虫类名
        cls = getattr(m,cls_name)
        # 初始化爬虫类
        return cls()
    @defer.inlineCallbacks
    def crawl(self,spider_cls_path):
        # 创建引擎，可以想象成爬虫的心脏
        engine = self._create_engine()
        # 加载spider
        spider = self._create_spider(spider_cls_path)
        # 由于start_requests中与yield关键字，因此是一个生成器。
        # 所以使用iter关键字让他生成迭代器
        # 将spider类的生成器start_requests变为迭代器
        start_requests = iter(spider.start_requests())
        # 将引擎打开，同时把迭代器放到引擎中
        yield engine.open_spider(start_requests)
        # 激活_close参数
        yield engine.start()
        pass

class CrawlerProcess(object):
    """
    defer 用于开启事件循环
    """
    def __init__(self):
        """
        _activate代表爬虫进程，一个集合
        """
        self._active = set()
    def crawl(self,spider_cls_path):
        """
        创建多个defer对象，将这些爬虫对象d放在_active集合中
        :return:
        """
        crawler = Crawler()
        #　加载spider到爬虫中，同时设置引擎等
        d = crawler.crawl(spider_cls_path)
        # 将爬虫对象放入集合中
        self._active.add(d)
        pass

    def start(self):
        # 将爬虫对象的集合放入deferlist中运行
        dd = defer.DeferredList(self._active)
        # 结束时运行reactor.stop
        dd.addBoth(lambda _:reactor.stop())
        # 开始运行
        reactor.run()
        pass

class Command(object):

    def run(self):
        # 建立一个爬虫进程
        crawlerProcess = CrawlerProcess()
        # 列出spider的路径
        spider_cls_path_list = [
            # "spider.chouti.ChoutiSpider",
            "spider.cnblogs.CnblogsSpider"
        ]
        # 将spider加载到爬虫中
        for spider_cls_path in spider_cls_path_list:
            crawlerProcess.crawl(spider_cls_path)
        # 运行crawler
        crawlerProcess.start()
        pass
if __name__ == "__main__":
    cmd = Command()
    # 从命令行开始运行
    cmd.run()