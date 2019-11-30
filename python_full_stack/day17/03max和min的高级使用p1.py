# -*- coding: utf-8 -*- 
# @Time : 2019/11/30 下午5:42 
# @Author : yangchengkai
# @File : 03max和min的高级使用p1.py

"""
主要讲了max比较可迭代对象时候，按照迭代时候对象的值的顺序进行大小排序的。
"""
# TODO 面试题，给一个字典如下，在一次循环内找到分数最高的学生，输出“name:”+"age."。
score = {
    "yck":19,
    "wsn":100,
    'forrst':89,
    'hary':88
}
print(max(zip(score.values(),score.keys())))