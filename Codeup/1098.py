h, w=map(int, input().split())
n=int(input())
pan=[[0]*w for _ in range(h)]
for _ in range(n):
    l, d, x, y=map(int, input().split())
    if d==0: #가로는 0 세로는 1
        rowIndex=x-1
        for width in range(0,l):
            pan[rowIndex][y-1+width]=1
    elif d==1:
        columnIndex=y-1
        for height in range(0,l):
            pan[x-1+height][columnIndex]=1

for i in pan:
    for j in i:
        print(j, end=' ')
    print()

"""
if d==0: #가로는 0 세로는 1
        rowIndex=x-1
        for width in range(y-1, y-1+l): 
            pan[rowIndex][width-1]=1
    elif d==1:
        columnIndex=y-1
        for height in range(x-1,x+l):
            pan[height-1][columnIndex]=1
"""