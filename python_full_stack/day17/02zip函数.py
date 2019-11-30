# -*- coding: utf-8 -*- 
# @Time : 2019/11/30 下午5:24 
# @Author : yangchengkai
# @File : 02zip函数.py

"""
zip是拉链的意思返回元祖的迭代器，参数也为n个迭代器。
"""
print(list(zip(('a','b','c'),('1','2','3'))))
# zip(iter1 [,iter2 [...]])
p = {'name':'alex','age':18,'gender':'none'}
print(list(zip(p.keys(),p.values())))

print(list(zip(range(10),'abcdefgh','123456789')))
