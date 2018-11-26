import random
def gnomesort(seq):
    print(seq)
    print("---------------")
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            print(i)
            print(str(seq[i-1])+" "+str(seq[i]))
            i += 1
            print(seq)
        else:
            print(i)
            seq[i], seq[i-1] = seq[i-1], seq[i]
            print(str(seq[i-1])+" "+str(seq[i]))
            i -= 1
            print(seq)
    print(seq)



gnomesort([random.randint(1,1000) for i in range(5)])