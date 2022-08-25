import sys

n=int(sys.stdin.readline().strip())
count=0
def box(x, y, n):
    global count
    print(count)
    if n//3!=0:
        for i in range(x, x+n, n//3):
            for j in range(y, y+n, n//3):
                box(0, 0, n//3)
                count+=1
        return
box(0, 0, n)