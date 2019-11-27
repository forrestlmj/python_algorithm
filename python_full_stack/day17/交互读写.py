# -*- coding: utf-8 -*- 
# @Time : 2019/11/27 下午3:34 
# @Author : yangchengkai
# @File : 交互读写.py

# s = open("write",'w',encoding='utf-8')
# data = s.read()
# s.close()

# with open("陈粒.txt",'r+',encoding='utf-8') as s,\
#     open("write_back",'w+',encoding='utf-8') as t:
#     d =s.read()
#     print(d)
#     t.write(d)

with open("陈粒.txt",'r+',encoding='utf-8') as s,\
    open("陈粒back.txt",'w',encoding='utf-8') as t:
    l = s.readlines()
    t.writelines(l[-2:])
