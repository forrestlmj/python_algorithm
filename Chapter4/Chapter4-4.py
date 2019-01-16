import random

def sel_sort_res(l,i):
    if i == 0:
        return
    max_j = i
    for j in range(i):
        if l[j] > l[max_j]:
            max_j = j
    l[max_j], l[i] = l[i], l[max_j]
    sel_sort_res(l, i-1)

l = [random.randint(0, 10) for i in range(0, 10)]
print(l)
sel_sort_res(l, len(l)-1)
print(l)

