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
"""
全局变量与局部变量
"""
name = "1hf"
def change_name():
    name = "yck"
    print("change name",name)
change_name()
print(name)
"""
加global关键字引用全局变量。
"""
def change_g_name():
    global name
    name = "1"
    print("change name",name)
print("globa "+name)
change_g_name()
print("globa "+name)
def pr():
    print("name",name)
l = ["yck","wsn"]

def ll():
    # 全局变量声明放在上面
    # global l
    l.append(1)
    print(l)
ll()

"""

global引用的是最外层的全局变量,而不是上一层的变量
"""
name = "刚娘"
def weihou():
    name = "陈卓"
    def weiweihou():
        global name
        name = "冷静"
    weiweihou()
    print(name)
print(name)
weihou()
print(name)
"""
如果想要使用上一层变量，则使用关键字nonlocal
"""
name = "刚娘"
def weihou():
    name = "陈卓"
    def weiweihou():
        nonlocal name #nonlocal找上级变量
        name = "冷静"
    weiweihou()
    print(name)
print(name)
weihou()
print(name)