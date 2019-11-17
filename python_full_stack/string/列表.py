"""
day11列表魔法相关
列表可嵌套，啥都能装,切片、索引与字符串一样
"""
l = [1,"yangck",[True,None],2,3,4]
# 与字符串不同：修改列表不会为列表新创建内存空间，因为列表可以看为一个链表，保存地址。
# 而字符串类似于连续空间的数组，需要每次修改时候重新申请内存。
# 修改
l[1] = 1
print(l)



#列表的构建：,当s是可迭代的，那么可以转为list,如果s=123那么肯定不行
s = "dsdf"
l = list(s)

# 复制,浅拷贝，重要
a = l.copy()

#　计算个数
print(l.count(1))
# extend,加可迭代对象,列表，迭代器，字符串，直接添加，append整体追加。
l.append([1,2])
print(l)
l.extend([1,2])
print(l)
l.extend("asas")
print(l)
l.extend((range(10)))
print(l)

#pop,默认删除最后一个值,指定索引删除
print(l.pop())
print(l.pop(1))
print(l)
print(l.pop(2))
print(l)
# remove按照值删除
print(l.remove(3))
#　删除,通过del关键字，通过切片或索引
del(l[1])
del l[1:3]
print(l)
# 清空
# l.clear()

l.reverse()
# print(l)
# l.sort()
print(l)
#TODO 排序
# sorted
# key,value,lambda