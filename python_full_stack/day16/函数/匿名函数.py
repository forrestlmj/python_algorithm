# -*- coding: utf-8 -*- 
# @Time : 2019/11/27 上午10:01 
# @Author : yangchengkai
# @File : 匿名函数.py
# lambda x:x+1
def calc(x):
    return x+1
res = calc(10)
print(res)

# 性参：表达式
print(calc)
# <function calc at 0x7fae2745e1e0>
print(lambda x:x+1)
# <function <lambda> at 0x7fae27383a60> 函数名<lambda>函数地址 0x7fae27383a60
f = lambda x:x+1
print(f(10))

# alex改为"alex_sb" （不应该这样用，）
f = lambda x:x+"_sb"
print(f("alex"))
# 1刚声明就释放。因为没有赋值，直接释放了，lambda也应该这样用。
1
# lambda不能有ifelsefor等
name1= ""
