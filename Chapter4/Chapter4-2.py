import random


def ins_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while j>0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1

l = [random.randint(0, 20) for i in range(5)]
print(l)
ins_sort(l)
print(l)