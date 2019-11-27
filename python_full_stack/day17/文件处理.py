# -*- coding: utf-8 -*- 
# @Time : 2019/11/27 下午3:11 
# @Author : yangchengkai
# @File : 文件处理.py
"""
打开文件得到句柄
通过句柄对文件处理
关闭

# 按照utf-8编码形式向操作系统获得文件的句柄，到内存也就是变量c
# python默认open方法是调用操作系统的编码方式
"""



# read读取所有到内存变量字符串
f = open('write',encoding='utf-8')
c = f.read()
print(c)
f.close()

# 每行读取
f = open('陈粒.txt',encoding='utf-8')
s = f.readline()
print(s)
print(f.readline())
print(f.readline())