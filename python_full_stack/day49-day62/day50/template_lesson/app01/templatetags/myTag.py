# -*- coding: utf-8 -*- 
# @Time : 2020/3/31 上午7:07 
# @Author : yangchengkai
# @File : myTag.py
from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter
def filter_multi(x, y):
    print(x,y)
    return x * y
