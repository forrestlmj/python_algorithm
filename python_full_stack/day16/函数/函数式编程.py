# -*- coding: utf-8 -*- 
# @Time : 2019/11/27 上午10:01 
# @Author : yangchengkai
# @File : 函数式编程.py
# lambda x:x+1


"""
编程方法类
#面向过程

#面向对象

#函数式 = 编程语言定义的函数+数学意义的函数
    def f(x):
        return 2*x+1
    函数体内不能用变量保存状态，不改变量。
    函数即变量
y = 2*x + 1

"""
# 函数即变量特性：
# 高阶函数两种情况：

# 1、把函数当作参数传给另一个函数
def foo(n):
    print(n)

def bar(name):
    print("ny n is %s" % name)

foo(bar)
foo(bar("xx"))

print ("********")
# 2、返回值包含函数
def foo():
    """

    :return:返回自己，变量。
    """
    print("from foo")
    return foo
print(foo())
c =  foo()
print(c())
# ##########重要！以后装饰器会用到高阶函数。