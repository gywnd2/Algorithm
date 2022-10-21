import sys
from collections import deque
n, m=map(int, sys.stdin.readline().strip().split())
ice=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

dx, dy=[-1, 1, 0, 0], [0, 0, -1, 1]
visited=[[False for _ in range(m)] for _ in range(n)]
q=deque()
time=0

def bfs():
    global time
    while q:
        x, y=q.popleft()
        visited[x][y]=True
        count=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and ice[nx][ny]==0:
                count+=1
        if count>=2:
            ice[x][y]=0
        # for row in ice:
        #     print(row)
        # print()
    time+=1

isIceExist=False
while True:
    for i in range(n):
        for j in range(m):
            if ice[i][j]==1:
                count=0
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if 0<=nx<n and 0<=ny<m and ice[nx][ny]==0:
                        count+=1
                if count>=2:
                    isIceExist=True
                    q.append((i, j))
    if not isIceExist:
        break
    isIceExist=False
    bfs()
print(time)   