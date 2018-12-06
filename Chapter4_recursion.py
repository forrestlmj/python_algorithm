import cProfile

def trav(seq, dep=0):
    if dep == len(seq):
        # print(seq[dep-1])
        abs(len(seq) - dep)
        return
    trav(seq, dep+1)
    print(seq[dep])
print(cProfile.run('trav(range(100))'))


