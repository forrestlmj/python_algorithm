# -*- coding: utf-8 -*- 
# @Time : 2019/12/5 下午2:58 
# @Author : yangchengkai
# @File : 03高阶函数使用.py

"""
1、参数是函数名
2、返回值是参数名
满足任何一个条件就是高阶函数。

"""
import time


def foo():
    time.sleep(0.5)
    print("hello")

def test(func):
    """
    高阶函数情况1,以函数名作为参数。
    :param func: 函数名
    :return: 无
    """
    print(func)
    start = time.time()
    func()
    end = time.time()
    print("函数运行时间：%s"%str(end-start))
test(foo)


def foo():
    print("from the foo")
def test(func):
    """
    返回值和参数名都是函数
    :param func:
    :return:
    """
    return func

res = test(foo)
res()
# 多运行了一步func不行。
def timmer(func):
    """
    高阶函数情况1,以函数名作为参数。
    :param func: 函数名
    :return: 无
    """
    print(func)
    start = time.time()
    func()
    end = time.time()
    print("函数运行时间：%s"%str(end-start))
    return func
foo = timmer(foo)
foo()
