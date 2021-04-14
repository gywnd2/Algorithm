from math import sqrt
m=int(input()); n=int(input())
squareNum=[]
for i in range(m, n+1):
    if int(sqrt(i))==sqrt(i):
        squareNum.append(i)
if squareNum==[]:
    print(-1)
else:
    print(sum(squareNum))
    print(min(squareNum))