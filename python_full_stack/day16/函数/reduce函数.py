# -*- coding: utf-8 -*- 
# @Time : 2019/11/27 上午11:52 
# @Author : yangchengkai
# @File : reduce函数.py

# TODO 计算num内的元素相乘，写一个reduce方法。
num = [1,2,3,100]
def reduce_test(func,array,init=None):
    if init is None:
        res = array.pop()
    else:
        res = init
    # res = array.pop(0)
    for num in array:
        res=func(res,num)
    return res

print(reduce_test(lambda x,y:x*y,num))
print(reduce_test(lambda x,y:x*y,num,2))


# reduce 函数计算阶乘
from functools import reduce
num_1 = [1,2,3,100]
print(reduce(lambda x,y:x*y,num_1))
# print(reduce(lambda x,y:x*y,num_1))

print(reduce(lambda x,y:x+y,range(10)))
print(reduce(lambda x,y:x+y,["ya","yasdf","sdf"]))