# -*- coding: utf-8 -*- 
# @Time : 2019/12/8 下午9:34 
# @Author : yangchengkai
# @File : 04函数闭包.py


def father(name):
    print('from father %s'%name)
    def son():
        print('from the son')
    print(locals())
father('alex')