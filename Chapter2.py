from Chapter2_test import find_table_index
def mylist():
    #
    nums = []
    # nums在python中为连续存储，因此append的存储效率较高 时间复杂度为O(1) insert为时间复杂度O(N)
    nums.append(1)
    nums.insert(0,2)
    # 程序评估时间
def mytime():
    import timeit
    x=1
    print(timeit.timeit("x=2+2"))
    print(timeit.timeit("x = sum(range(100))"))
    import cProfile
    cProfile.run('find_table_index("D://原生docx//安投（北京）金融信息服务有限公司_自查报告（word文字版）.docx","运营总体情况")')
def myhash():
    # dict与set set的值为hash table dict的key值为hash table TODO 待验证dict 的keyhash值
    print(hash(42))
    print(hash("Hello World"))
    print(hash("Hello world"))
def mytype(a):
    print(type(a))
    print(a)
# range类型 与list初始化
def myRangeAndList():
    a = range(10)
    mytype(a)
def graphy():
    # 邻接列表 邻接集
    a, b, c, d, e, f, g, h = range(8)
    N = [
        {b, c, f, d, e},     # a
        {c, e},              # b
        {d},                 # c
        {e},                 # d
        {f},                 # e
        {c, g, h},              # f
        {f, h},              # g
        {f, g},              # h
    ]
    print(b in N[a])
    print(d in N[c])
    print(N[f])

graphy()