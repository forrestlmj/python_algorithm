# -*- coding: utf-8 -*- 
# @Time : 2019/12/3 下午3:55 
# @Author : yangchengkai
# @File : 03文件操作的其他方式.py
f = open('a.txt','r+',encoding='gbk')
print(f.read())
# f.write('你好')
print(f.closed)
print(f.encoding)
# f.write()
f2 = open('b.txt','r',encoding='utf-8',newline='')
print(f2.encoding)
print(f2.read())


# flush将内存中数据同步到磁盘。
# f.flush
# 光标位置2
print(f2.tell())
# seek代表字节，3代表一个汉字单位。
f2.seek(3)
print(f2.readlines())
# 截取字节10个truncate
f3 = open('b.txt','r+',encoding='utf-8',newline='')

print( f3.truncate(10))




