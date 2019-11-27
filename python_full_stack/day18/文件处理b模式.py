# -*- coding: utf-8 -*- 
# @Time : 2019/11/27 下午4:07 
# @Author : yangchengkai
# @File : 文件处理b模式.py

# b模式就是直接把磁盘中字节读到内存中再解码，而不是b形式则是在open时候直接按照指定的编码格式解码。
# 在open中如果采用bytes字节进行磁盘读取时候，就不要指定encoding编码格式，而是直接用b形式。
with open("陈粒.txt",'rb') as f:
    c = f.read()
    print(type(c))
    print(c)
    # 内存到磁盘编码为字节码，磁盘到内存，按照编码集解码
    print(c.decode('utf-8'))
# 从变量也就是内存写到磁盘中，使用encode编码
f = open('ttt.txt','wb')
f.write('你好'.encode('utf-8'))


f = open()
