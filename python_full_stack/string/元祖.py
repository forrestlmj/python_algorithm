"""
day12元祖
元素不能修改、增加、删除
"""
# tuple
tu = (111,"111",[1,2,3],44,)
# 切片
print(tu[1:2])
# for，可迭代对象，元祖、列表、字符串可互相转换。
print(list(tu))
print(tuple([1,2,3]))
#元祖的一级元素不可修改
tu[2][1] = 1212
print(tu)

# 元祖转换为列表后，再修改值，再换回来
t = list(tu)
t.pop()
print(tuple(t))