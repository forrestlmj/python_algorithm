# -*- coding: utf-8 -*- 
# @Time : 2019/11/27 下午3:23 
# @Author : yangchengkai
# @File : 文件写.py

f = open("write",'w',encoding='utf-8')
f.write("sss")
f.writelines("nextline")
f.writelines(["aa\n","bbb\n",'ccc\n'])



