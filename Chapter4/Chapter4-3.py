import random


def sel_sort(l):
    for i in range(len(l)-1, 0, -1):
        max_j = i
        for j in range(0,i):
            if l[j] > l[max_j]:
                max_j = j
        l[i],l[max_j] = l[max_j],l[i]
l = [random.randint(0,10) for i in range(0,10)]
print(l)
sel_sort(l)
print(l)