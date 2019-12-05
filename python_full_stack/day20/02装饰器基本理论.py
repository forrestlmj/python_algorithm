# -*- coding: utf-8 -*- 
# @Time : 2019/11/29 上午10:51 
# @Author : yangchengkai
# @File : 02装饰器基本理论.py

"""
装饰器 = 高阶函数+函数嵌套（跨作用域，能取到上层）+闭包（函数内只有自己的变量）

装饰器：本质是函数，功能为其他函数添加附加功能
1、不修改被修饰函数的源代码
2、不修改被修饰函数的调用方式
"""
import time
def timmer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print("运行了%s" % str(end - start))
    return wrapper
@timmer
def cal(l):
    r = 0
    for i in l:
        time.sleep(0.1)
        r += 1
    print(r)
    return r

print(cal(range(25)))