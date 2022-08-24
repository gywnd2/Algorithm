import sys

n=int(sys.stdin.readline().strip())
paper=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

minus=0; zero=0; one=0
def check(x, y, n):
    global minus, zero, one
    num=paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j]!=num:
                for k in range(3):
                    for l in range(3):
                        check(x+k*n//3, y+l*n//3, n//3)
                return
    if num==1:
        one+=1
    elif num==-1:
        minus+=1
    elif num==0:
        zero+=1
        
check(0, 0, n)    
print(minus)
print(zero)
print(one)