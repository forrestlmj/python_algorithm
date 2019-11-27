# -*- coding: utf-8 -*- 
# @Time : 2019/11/27 上午11:37 
# @Author : yangchengkai
# @File : filter函数.py

"""
与map方法很相似，只不过filter的函数变量的返回结果必须为Boolean值，因为是过滤方法。

"""
movie_people = ['sb_alex','sb_wupeiqi','linhaifeng','sb_yuanhao']
print(list(filter(lambda _:not _.startswith('sb'),movie_people)))