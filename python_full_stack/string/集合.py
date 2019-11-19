# day14集合
# 不同元素组成（去重）
# 集合无序的
# 集合中必须是不可变类型，
s = set()
s.add(1)
s.add(2)
s.add("1")
s.pop()
# 删除
s.remove("1")
s.discard("1")
"""
        Remove an element from a set if it is a member.

        If the element is not a member, do nothing.
        """
s.discard("sdf")
# s.update({1:5})
print(s)
############# 集合关系
python_l = ["lcg","szw","zjw","lcg"]
linux_l = ["lcg","szw","ycl"]
p_s = set(python_l)
l_s = set(linux_l)
# 交集
print(p_s.intersection(l_s))
print(p_s & l_s)
# 并集
print(p_s.union(l_s))
print(p_s|l_s)
# 差集
print(p_s.difference(l_s))
print(p_s - l_s)
# 交叉补集
print(p_s.symmetric_difference(l_s))
print(p_s^l_s)

print(p_s.difference_update(l_s))

a,b = {1,2},{2,3,5}
print(a.isdisjoint(b))
print({1,2}.issubset({1,2,3}))
# 更新多个值
a.update(b)
print(a)


# 交并差补
# & | - ^

# 不可变set
s=frozenset((1,23))
print(s)
