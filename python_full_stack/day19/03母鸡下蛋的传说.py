# -*- coding: utf-8 -*- 
# @Time : 2019/12/3 下午9:01 
# @Author : yangchengkai
# @File : 03母鸡下蛋的传说.py
#
def product_baozi():
    for i in range(100):
        yield '下蛋 %s' % i
g = product_baozi().__iter__()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))