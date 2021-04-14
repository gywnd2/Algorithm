abc=list(int(input()) for _ in range(3))
mul=abc[0]*abc[1]*abc[2]
num=list(0 for i in range(0, 10))
mul=str(mul)

for i in range(len(mul)):
    num[int(mul[i])]+=1

for i in range(10):
    print(num[i])