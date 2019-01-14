# 清单4-1 递归版的插入排序
import random


def ins_sort_rec(seq, i):
    if i == 0 : return
    ins_sort_rec(seq, i - 1)
    j = i
    while j > 0 and seq[j - 1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1


l = [random.randint(0, 20) for i in range(5)]
print(l)
ins_sort_rec(l, len(l)-1)
print(l)
