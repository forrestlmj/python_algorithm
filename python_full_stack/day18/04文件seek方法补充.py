# -*- coding: utf-8 -*- 
# @Time : 2019/12/3 下午7:44 
# @Author : yangchengkai
# @File : 04文件seek方法补充.py

"""
seek与tell的高端玩法
"""

f = open("seek.txt",'rb')
print(f.tell())
f.seek(10,0)
print(f.tell())
f.seek(3,1)
print(f.tell())

