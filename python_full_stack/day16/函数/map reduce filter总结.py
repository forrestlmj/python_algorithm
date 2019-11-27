# -*- coding: utf-8 -*- 
# @Time : 2019/11/27 上午11:58 
# @Author : yangchengkai
# @File : map reduce filter总结.py

p = [
    {'n':'alex','age':18},
    {'n': 'wupei', 'age': 30},
    {'n': 'li', 'age': 28},
    {'n': 'linhan', 'age': 34},

]
#使用filter获得年龄小于30的员工。
print(list(filter(lambda _:_.get('age')<30,p)))
from functools import reduce