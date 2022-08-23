import sys

n=int(sys.stdin.readline().strip())
paper=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

minus=0
zero=0
one=0

def total(r, c):
    tmp=sum(paper[r][c:c+3])
    tmp+=sum(paper[r+1][c:c+3])
    tmp+=sum(paper[r+2][c:c+3])
    return tmp

for i in range(0, n, 3):
    for j in range(0, n, 3):
        totalSum=total(i, j)
        if totalSum==0:
            print("zero!")
            zero+=1
        elif totalSum==9:
            print("one!")
            one+=1
        elif totalSum==-9:
            print("minus!")
            minus+=1
        else:
            print('error!')