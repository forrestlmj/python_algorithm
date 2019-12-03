# -*- coding: utf-8 -*- 
# @Time : 2019/11/27 下午9:02 
# @Author : yangchengkai
# @File : 07三元表达式列表解析生成器表达式.py


"""
生成器是一种数据类型，已经符合了迭代器协议。

"""
"""
生成器函数：
含有yield关键字。
"""
def foo():
    yield 1

c = foo
print(type(c))
print(c)
d = c()
print(d)
print(d.__next__())

"""
生成器表达式与三元表达式
"""
n = "1"
c = 'SB' if n == 's' else 'smart'

# 三元表达式，生成100以内偶数:三元表达式,这个结合列列表推倒
l = [i for i in range(100) if i%2 == 0]
print(l)

# 生成一个10000000以内的偶数，这里不能直接列表推导，而是要用生成器。
l_iter = (i for i in range(10) if i%2 == 0)
print(l_iter)
print(l_iter.__next__())
print(l_iter.__next__())
print(l_iter.__next__())

word_l = ["yck","yangchengkai","wsn","wangshengnan"]
l2 = ("".join(list(map(lambda _:_+"_",i))) for i in word_l if "k" in i)
print(next(l2))
print(next(l2))


print(sum((i for i in range(10000000000000000))))