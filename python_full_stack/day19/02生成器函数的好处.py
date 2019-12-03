# -*- coding: utf-8 -*- 
# @Time : 2019/12/3 下午8:40 
# @Author : yangchengkai
# @File : 02生成器函数的好处.py


def product_baozi():
    for i in range(100):
        yield '一屉包子 %s' % i
g = product_baozi().__iter__()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))