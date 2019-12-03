# -*- coding: utf-8 -*- 
# @Time : 2019/12/3 下午3:30 
# @Author : yangchengkai
# @File : 05其他内置函数.py
print(chr(97))
print(ord('a'))
# 平方
print(pow(10,3))
l = [1,2,3,4]
# 倒叙
print(list(reversed(l)))

print(round(4.5))

l = 'hello'
s = slice(1,4,2)
print(l[s])

# 排序,d为可迭代对象，key为函数
d = [{'name':'yck','age':20},
     {'name':'wsn','age':18},
     {'name':'jud','age':10}]

print(sorted(d,key=lambda _:_.get('age')))

name = {
    'alex':200,
    'wupei':300,
    'yuanhoa':900
}
print(sorted(name,key=lambda k:name[k]))

# locals
def test():
    msg = 'sf'
    print(locals())
test()


# import通过字符串的方式。
m_a = 'test2'
m = __import__(m_a)
m.say_hi()