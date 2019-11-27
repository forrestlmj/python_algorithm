# -*- coding: utf-8 -*- 
# @Time : 2019/11/26 上午9:40 
# @Author : yangchengkai
# @File : request.py


# weakref为弱引用的一个库，当没有指针指向该引用时，则回收该对象。
_fingerprint_cache = weakref.WeakKeyDictionary()
def request_fingerprint(request, include_headers=None):
    """
    对请求的链接进行标准化，使用sha1对请求生成信息摘要，最后返回指纹
    :param request:请求
    :param include_headers:是否包含请求头
    :return:返回信息摘要的16进制形式的字符串值
    """
    # 一般在调用的时候，这里设置为None。
    if include_headers:
        # 把header中每项取出，转换为二进制类型，便于之后加密
        include_headers = tuple(to_bytes(h.lower())
                                 for h in sorted(include_headers))
    # 获得弱引用
    cache = _fingerprint_cache.setdefault(request, {})
    if include_headers not in cache:
        # 指定hash算法为sha1
        fp = hashlib.sha1()
        # 编码方法、转为二进制并hash
        fp.update(to_bytes(request.method))
        # 标准化、链接，转为二进制并hash
        fp.update(to_bytes(canonicalize_url(request.url)))
        # hash请求body
        fp.update(request.body or b'')
        if include_headers:
            for hdr in include_headers:
                if hdr in request.headers:
                    fp.update(hdr)
                    for v in request.headers.getlist(hdr):
                        fp.update(v)
        # 返回信息摘要的16进制形式的字符串值
        cache[include_headers] = fp.hexdigest()
    return cache[include_headers]
