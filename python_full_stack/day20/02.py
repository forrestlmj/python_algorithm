# -*- coding: utf-8 -*- 
# @Time : 2019/11/29 上午10:51 
# @Author : yangchengkai
# @File : 02.py

"""
装饰器 = 高阶函数+函数嵌套（跨作用域，能取到上层）+闭包（函数内只有自己的变量）


"""
import time
def cal(l):
    s_time = time.time()
    r = 0
    for i in l:
        time.sleep(0.1)
        r += 1
    stop_time = time.time()
    print("运行时间：%s" % (stop_time-s_time))
    return r

ame = 1
def x():
    print(ame)

x()