from collections import deque
import sys

n=int(sys.stdin.readline().strip())
image=[list(sys.stdin.readline().strip()) for _ in range(n)]
res=[]
def check(x, y, n):
    num=image[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if image[i][j]!=num:
                res.append("(")
                for k in range(2):
                    for l in range(2):
                        tmp=check(x+k*n//2, y+l*n//2, n//2)
                        if tmp!=None:
                            res.append(tmp)
                res.append(")")
                return
    res.append(num)
    return
            
check(0, 0, n)
print("".join(res))