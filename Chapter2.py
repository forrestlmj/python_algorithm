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
    print("------列表------")
    a, b, c, d, e, f, g, h = range(8)
    N2 = [
        [b, c, f, d, e],     # a
        [c, e],              # b
        [d],                 # c
        [e],                 # d
        [f],                 # e
        [c, g, h],              # f
        [f, h],              # g
        [f, g],              # h
    ]
    print( b in N2[a])
    a, b, c, d, e, f, g, h = range(8)
    N3 = [
        {b: 2, c: 1, d: 3, e: 9, f: 4},  # a
        {c: 4, e: 3},                     # b
        {d: 8},                              # c
        {e: 7},                             # d
        {f: 5},                             # e
        {c: 2, g: 2, h: 2},                 # f
        {f: 1, h: 6},                       # g
        {f: 9, g: 8}                        # h
    ]
    print(b in N3[a])
    print(len(N3[f]))
    print(N3[a][b])
# 调度临界矩阵
graphy()
def matrix():
    a, b, c, d, e, f, g, h = range(8)
    # a, b, c, d, e, f, g, h
    N = [[0, 1, 1, 1, 1, 1, 0, 0], # a
         [0, 0, 1, 0, 1, 0, 0, 0], # b
         [0, 0, 0, 1, 0, 0, 0, 0], # c
         [0, 0, 0, 0, 1, 0, 0, 0], # d
         [0, 0, 0, 0, 0, 1, 0, 0], # e
         [0, 0, 1, 0, 0, 0, 1, 1], # f
         [0, 0, 0, 0, 0, 1, 0, 1], # g
         [0, 0, 0, 0, 0, 1, 1, 0]  # h
         ]
    print(N[d][f])
    print(sum(N[h]))
matrix()

# 树
T = [["a", "b"], ["c"], ["d", ["d", ["f"]]]]
print(T[0][1])
class Tree:
    def __init__(self,left,right):
        self.left = left
        self.right = right
t = Tree(Tree("a", "b"), Tree("c", "d"))
print(t.left.right)