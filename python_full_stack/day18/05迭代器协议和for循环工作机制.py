# -*- coding: utf-8 -*- 
# @Time : 2019/11/27 下午5:15 
# @Author : yangchengkai
# @File : 05迭代器协议和for循环工作机制.py

x = "yagc"
c = x.__iter__()
print(next(c))
print(next(c))
print(next(c))

# 字典、列表、字符串本不是迭代器，但他们遵循迭代器协议。但是for循环中调用它的__iter__()
l = [1,2,3,4,5]

# for循环就是基于迭代器协议实现的，进行遍历的。
for i in l:
    # i = l.__iter__()
    # 之后　调用i.__next__()方法。
    print(i)

c = l.__iter__()# 将遵循迭代器协议的对象，转换为迭代器对象。
print(c.__next__())


"""
重点！！！：
for提供了一个可以遍历所有对象的机制——因为它基于迭代器协议进行，
不需要有索引，只需要__next__()方法，时间复杂度可以理解为O(n)。
而while循环则是使用索引，时间复杂度为O(1)

"""
l = {1,23,4,5,6,7,5,2}
# 如果使用while循环遍历无序数据类型，则需要自己初始化迭代器，处理StopIteration方法。
c = iter(l)
d = c.__iter__()
while True:
    try:
        print(d.__next__())
    except StopIteration:
        break

"""
补充，迭代器就是可迭代对象。一个数据类型如果有__iter__方法，那么它就可以生成迭代器   。
"""

f = open("ttt.txt",encoding='utf-8')
i = f.__iter__()
print(i.__next__(),end="")
print(i.__next__())
