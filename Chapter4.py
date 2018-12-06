# 第四章归纳、递归以及归简 Udi Manber <<Using induction to design algorithm>>
import cProfile
import timeit
from random import randrange
# 暴力检索，两次遍历数组，计算出差值，得到最小差值时候的两个数字，复杂度O(N^2)
def find_1(l):
    dd = float('inf')

    for x in l:
        for y in l:
            if x == y:
                continue
            d = abs(x-y)
            if d < dd:
                xx, yy, dd = x, y, d
    print(str(xx)+","+str(yy))
    print("复杂度O(N^2)")
# 由于数列是随机的，因此可以先排序O(NlogN)，然后只遍历一次数组O(N)，计算前后值的差值，O(NlogN)+O(N) = O(NlogN)
def find_2(l):
    print("复杂度O(NlogN)")
if __name__ == "__main__":
    # 在一个随机数列中，找出距离最相近且不相等的两个数字
    l = [randrange(10**10) for i in range(10000)]
    print(cProfile.run('find_1(l)'))

