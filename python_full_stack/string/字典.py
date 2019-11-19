"""
day12字典
元素不能修改、增加、删除
"""
info = {
    "k1":"v1", # 键值对
    "k2":"v2"
}
# 字典的key必须是hashable的，字典、列表不能作为key

info2 = {
    True:"True",
    False:"False"
}
print(info2)
# 字典使用del删除

# 迭代
for k in info:
    print(k,info[k])
for k,v in info.items():
    print(k,v)
for k in info.keys():
    print(k)
for v in info.values():
    print(v)

# dict的方法：
# fromkeys静态方法,arg1可迭代变量作为类，arg2值
v = dict.fromkeys(["k1",1,True])
print(v)
v = dict.fromkeys("abcd",True)
print(v)

# get
print(v.get("notk"))
print(v.get("notk","default"))
# pop 指定k,删除
print(v.pop("k1","default"))

v.update(k2="newv2",k3="v3")
print(v)