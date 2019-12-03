# -*- coding: utf-8 -*- 
# @Time : 2019/12/3 下午8:19 
# @Author : yangchengkai
# @File : 01生成器函数.py
def test():
    print("this is 1")
    yield 1
    print("this is 2")

    yield 2
    yield "yck"
    yield "sdf"
g = test()
print(next(g))
print(next(g))
print(next(g))
print(next(g))