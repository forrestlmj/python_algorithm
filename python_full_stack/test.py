# https://www.youtube.com/watch?v=v64Z9s9hakE&t=215s
from twisted.internet import defer
from twisted.web.client import getPage
from twisted.internet import reactor


def stop(*args,**kwargs):
    reactor.stop()
def download(*args,**kwargs):
    print (args,kwargs)

@defer.inlineCallbacks
def task(url):
    v = getPage(url)
    v.addBoth(download)
    yield v
if __name__ == "__main__":
    url_list = [
        "http://www.baidu.com",
        "http://www.biying.com",
        "http://dig.chouti.com"
    ]
    _activate = set()
    for url in url_list:
        d = task(url)
        _activate.add(d)
    dd = defer.DeferredList(_activate)
    dd.addBoth(stop)
    reactor.run()