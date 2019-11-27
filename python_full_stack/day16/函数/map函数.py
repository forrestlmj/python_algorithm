# -*- coding: utf-8 -*- 
# @Time : 2019/11/27 上午11:08 
# @Author : yangchengkai
# @File : map函数.py
# map是高阶函数，因为传入的参数是方法。


# TODO 面试题要求实现map方法，方法包括+1,平方，/2：

def add(n):
    return n+1
def p(n):
    return n**2
def div(n):
    return n/2

def my_map(fuc,list):
    re = []
    for i in list:
        re.append(fuc(i))
    return re
a = [1,2,3,4,5]

print(my_map(add,a))
print(my_map(p,a))
print(my_map(div,a))

# a数据量超级大，
# 结合匿名参数：更厉害，因为直接把匿名函数作为变量发给方法。
print(my_map(lambda _:_+1,a))
print(my_map(lambda _:_**2,a))
print(my_map(lambda _:_/2,a))

# TODO 面试题：map怎么用？
"""
class map:
    def __init__(self,f,*iterable):
        
本质上也是迭代器，实现了__iter__与__next__，
"""
print("map 迭代器对象:",map(lambda _:_**2,a))
print("map 迭代器对象加列表推到:",list(map(lambda _:_**2,a)))

"""
    知识点
    map是迭代器类
    参数1为函数变量，有名或匿名函数，参数2为可迭代对象
    在2中迭代1的方法，返回迭代器
    
"""