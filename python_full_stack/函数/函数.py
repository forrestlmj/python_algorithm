def test4():
    return 1,23,4

test = test4()

print(test)

"""
可变长参数
"""
# 参数组：**字典，*列表
# 一个*代表列表
def test(x,*args):
    print(x)
    for i in args:
        print(i)

test(1,2,3,4)

def test1(x,**kwargs):
    for k,v in kwargs.items():
        print(k,v)

test1(1,y=2,z=4)

def test2(x,*args,**kwargs):
    print(x)
    for i in args:
        print(i)
    for k,v in kwargs.items():
        print(k,v)

test2(1,2,3,4,y=1,d=2)