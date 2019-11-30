# -*- coding: utf-8 -*- 
# @Time : 2019/11/29 上午11:49 
# @Author : yangchengkai
# @File : 05函数闭包装饰器基本实现.py
# 装饰器的架子
import time
def timmer(func):
    # 高阶函数 函数传参与返回。
    # 嵌套
    def wrapper():
        # print(func)
        start_time = time.time()
        func()
        stop_time =time.time()
        print("运行时间%s"%(stop_time-start_time))
    return wrapper


def test():
    time.sleep(3)
    print("end")
test = timmer(test)

test()