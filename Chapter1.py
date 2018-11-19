count = 10**5
num = []
for i in range(count):
    num.append(i)
num.reverse()
# insert效率反而较低
num2 = []
for i in range(count):
    num2.insert(0,i)
