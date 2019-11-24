# encoding=utf-8
from twisted.internet import reactor   # 事件循环（终止条件，所有的socket都已经移除）
from twisted.web.client import getPage # socket对象（如果下载完成，自动从时间循环中移除...）
from twisted.internet import defer     # defer.Deferred 特殊的socket对象 （不会发请求，手动移除）
from queue import Queue

class Request(object):
    """
    用于封装用户请求相关信息
    """
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
        """
        消费端，请求出队列
        :return:请求
        """
        try:
            req = self.q.get(block=False)
        except Exception as e:
            req = None
        return req

    def enqueue_request(self,req):
        """
        生产端，请求入队列
        :param req: 请求
        :return:
        """
        self.q.put(req)

    def size(self):
        return self.q.qsize()

class ExecutionEngine(object):
    """
    引擎：所有调度
    """
    def __init__(self):
        # 结束标志，当所有爬虫结束时候，设置此标识
        self._close = None
        # 引擎内部的调度器，用于缓存链接
        self.scheduler = None
        # 并发最大数量
        self.max = 5
        # 并发队列，引擎正在抓取的链接存放在这里，crawlling的长度要小于self.max
        self.crawlling = []
    def get_response_callback(self,content,request):
        """
        下载后的内容，经由此方法处理传给我们自定义的爬虫。爬虫返回的链接，则加入到调度器中
        :param content:网页文本内容
        :param request: 原始请求链接
        :return:
        """
        # 从并发队列中移除这个已经下载好的request
        self.crawlling.remove(request)
        # 将content和request实例化为response
        response = HttpResponse(content,request)
        # 这一步的request的callback十分重要，它就是我们方法中定义的callback方法：parse_xxx，这里把response传递给parse_xxx方法
        result = request.callback(response)
        # 获得result对象，也就是我们parse_xxx中return或者yield的方法
        import types
        # 如果result是生成器类型，这里就认为是新的请求（暂时不考虑Item的情况）
        if isinstance(result,types.GeneratorType):
            # 将生成器中的值取出，多个值的话迭代放入到调度器的队列中。
            for req in result:
                self.scheduler.enqueue_request(req)

    def _next_request(self):
        """
        类似递归方法，不断的从调度器中拿请求，然后再回调自己
        :return:
        """
        # 如果调度器为空并且抓取队列也为空，为_close设置callback为None参数，返回表示结束
        if self.scheduler.size() == 0 and len(self.crawlling) == 0:
            self._close.callback(None)
            return
        # 如果当前抓取队列中请求数量，小于阈值，则从调度器中取出新请求下载。同时最后回调自己。
        while len(self.crawlling) < self.max:
            # 从迭代器取出请求
            req = self.scheduler.next_request()
            # 如果请求为空，则返回
            if not req:
                return
            # 请求放入下载队列中
            self.crawlling.append(req)
            # 实际下载，这里对下载器做了简化，只调用getPage方法进行下载
            # 这里通过while循环指定了twisted中的defer数量，实现了并发。
            d = getPage(req.url.encode('utf-8'))
            # 下载结果传入自己的方法get_response_callback，进行下一步解析以及链接发现
            d.addCallback(self.get_response_callback,req)
            # 这里由于d已经完成了getPage的下载任务，因此，将d继续增加Callback到本身的方法
            # 以此保证并发数不变
            d.addCallback(lambda _:reactor.callLater(0,self._next_request))

    @defer.inlineCallbacks
    def open_spider(self,start_requests):
        # 实例化调度器
        self.scheduler = Scheduler()
        # 激活调度器
        yield self.scheduler.open()
        # 迭代种子列表生成器，将每个请求放入调度器中。
        while True:
            try:
                req = next(start_requests)
            except StopIteration as e:
                break
            self.scheduler.enqueue_request(req)
        # 处理完种子列表后，立刻调用自己的方法_next_request
        reactor.callLater(0,self._next_request)

    @defer.inlineCallbacks
    def start(self):
        self._close = defer.Deferred()
        yield self._close

class Crawler(object):
    """
    用户封装调度器以及引擎的...
    """
    def _create_engine(self):
        """
        每个爬虫创建一个引擎。
        :return:
        """
        return ExecutionEngine()

    def _create_spider(self,spider_cls_path):
        """

        :param spider_cls_path:  我们定制的Spider的路径
        :return:
        """
        # 分割出代码的路径，Spider的类名
        module_path,cls_name = spider_cls_path.rsplit('.',maxsplit=1)
        import importlib
        # 使用importlib包导入代码路径
        m = importlib.import_module(module_path)
        # 获得Spider类名
        cls = getattr(m,cls_name)
        # 返回Spider类的实例
        return cls()

    @defer.inlineCallbacks
    def crawl(self,spider_cls_path):
        # 获得引擎实例
        engine = self._create_engine()
        # 获得Spider实例
        spider = self._create_spider(spider_cls_path)
        # 获得Spider种子列表的生成器
        start_requests = iter(spider.start_requests())
        # 调用引擎的open_spider方法，传入种子列表的生成器
        yield engine.open_spider(start_requests)
        # 调用引擎的start方法
        yield engine.start()

class CrawlerProcess(object):
    """
    开启事件循环
    """
    def __init__(self):
        """
        用一个集合类变量，存放每个Spider形成的Crawler爬虫。
        """
        self._active = set()

    def crawl(self,spider_cls_path):
        """
        :param spider_cls_path:爬虫的路径
        :return:无
        """
        # 主要将我们写的spider实例化成一个个Crawler类
        crawler = Crawler()
        # 调用类方法，返回一个defer的生成器
        d = crawler.crawl(spider_cls_path)
        # 将Crawler的defer生成器到类变量中。
        self._active.add(d)

    def start(self):
        # 将集合中的每个Crawler类放入DefferedList
        dd = defer.DeferredList(self._active)
        # 当所有defer中的对象完成后，stop
        dd.addBoth(lambda _:reactor.stop())
        # 开始运行
        reactor.run()

class Commond(object):

    def run(self):
        # 实例化一个爬虫进程。
        crawl_process = CrawlerProcess()
        # 列出我们写的解析Spider的位置。
        spider_cls_path_list = ['spider.chouti.ChoutiSpider',
                                'spider.cnblogs.CnblogsSpider',]
        for spider_cls_path in spider_cls_path_list:
            # 将这些Spider的位置依次放入到爬虫进程中。
            crawl_process.crawl(spider_cls_path)
        # 开启爬虫进程
        crawl_process.start()


if __name__ == '__main__':
    """
    程序入口：命令方法
    """
    cmd = Commond()
    # 直接运行，原Scrapy中这里有runspider,crawl等方式。这里简化为run()方法。
    cmd.run()

