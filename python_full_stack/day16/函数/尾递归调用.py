# -*- coding: utf-8 -*- 
# @Time : 2019/11/27 上午10:52 
# @Author : yangchengkai
# @File : 尾递归调用与尾递归调用优化.py
# “尾递归调用”比“递归调用”要好，因为尾递归最后一步运行代码，不用保留“调用栈”
#　TODO 调用栈，尾递归


# “尾调用”是指方法最后一步调用，而不是最后一行，

# 不是为“尾调用”，foo最后一步方法为+1
def bar(n):
    return (n)
def foo(x):
    return bar(x)+1

# TODO 尾调用优化