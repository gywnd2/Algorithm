import sys

n=int(sys.stdin.readline().strip())
paper=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

white, blue=0, 0

def check(x, y, n):
    global white, blue
    
    num=paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j]!=num:
                for k in range(2):
                    for l in range(2):
                        check(x+k*n//2, y+l*n//2, n//2)
                return
    if num==0:
        white+=1
    elif num==1:
        blue+=1
    
check(0, 0, n)
print(white)
print(blue)