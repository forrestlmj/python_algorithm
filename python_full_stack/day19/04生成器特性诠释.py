# -*- coding: utf-8 -*- 
# @Time : 2019/12/5 下午12:04 
# @Author : yangchengkai
# @File : 04生成器特性诠释.py


# print(sum(i for i in range(10000000)))
"""
生成器函数：
1、语法与函数相似
2、自动实现迭代器协议
3、状态挂起，yield挂起生成器函数的状态，保留足够的信息

优点：
1、延迟计算，（sum运算）
2、提高可读性
"""
# TODO 面试题模拟，有一个几百g的大文件(人口.txt)，文件中每行是一个字典，要求求出其中人口的平均值
def ge(file = '人口.txt'):
    with open(file,'r',encoding='utf-8') as f:
        for i in f:
            yield eval(i)
def main():
    """

    :return:
    """
    g = ge()
    s = sum(i.get('pop') for i in g)
    print(s)

    c = ge()
    for i in c:
        print("city %s,population percent: %0.5s%%" % (i.get('city'),str(i.get('pop')/s*100)))
if __name__ == "__main__":
    main()