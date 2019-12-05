# -*- coding: utf-8 -*- 
# @Time : 2019/12/5 下午1:05 
# @Author : yangchengkai
# @File : 05生产者消费者模型.py
import time


def producer():
    n = 0
    while True:
        time.sleep(0.1)
        yield "第%s个包子"%str(n)
        n+= 1
def producer_confirm():
    n = -1
    while True:
        time.sleep(0.4)
        re = yield "第%s个包子"%str(n)
        n+= 1
        print("收到顾客%s的付款"%str(re))
def consumer(it = 100):
    p = producer()
    for i in range(it):
        print("顾客"+str(i)+"吃了:"+next(p))
def consumerAndConfirm(it = 100):
    p = producer_confirm()
    p2 = producer_confirm()
    # 注意send最开始是激活生成器作用，因此要传None或使用next方法
    p.send(None)
    p2.send(None)
    for i in range(it):
        print("顾客在p店"+str(i)+"吃了:"+p.send(i))
        print("顾客在p2店"+str(i)+"吃了:"+p2.send(i))

# consumer(20)
for i in range(10):
    print("-------------")
consumerAndConfirm(4)