import sys
from collections import deque
r,c=map(int, sys.stdin.readline().strip().split())
world=[list(sys.stdin.readline().strip()) for _ in range(r)]
visitedT=[[False for _ in range(c)] for _ in range(r)]
visitedR=[[False for _ in range(c)] for _ in range(r)]
qr, qt=deque(), deque()
dx, dy=[-1, 1, 0, 0], [0, 0, -1, 1]
time=0

def rain():
    while qr:
        x, y=qr.popleft()
        visitedR[x][y]=True
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<r and 0<=ny<c and not visitedR[nx][ny] and world[nx][ny]='.':
                visitedR[nx][ny]=True
                qr.append((nx, ny))
                world[nx][ny]='*'

def tb():
    while qt:
        x, y=qt.popleft()
        visitedT[x][y]=True
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<r and 0<=ny<c and not visitedT[nx][ny]:
                if world[nx][ny]=='.':
                    visitedT[nx][ny]=True
                    qt.append((nx, ny))
                    world[nx][ny]='W'
                    return 1
                elif world[nx][ny]=='H':
                    return 2


for row in range(r):
    for column in range(c):
        if world[row][column]=='*':
            qr.append((row, column))
            rain()
        elif world[row][column]=='W':
            qt.append((row, column))
            if tb()==1:
                pass
            elif tb()==2:
                continue
        time+=1
            
if time>0:
    print(time)
else:
    print('FAIL')