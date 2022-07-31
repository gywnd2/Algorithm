from collections import deque
import sys

n=int(sys.stdin.readline().strip())

apt=[list(sys.stdin.readline().strip()) for _ in range(n)]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
aptlist=[]

def bfs():
    count=1
    while q:
        x, y=q.popleft()
        # 시작점 방문처리 잊지않기!
        apt[x][y]='0'
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and apt[nx][ny]=='1':
                q.append((nx, ny))
                count+=1
                apt[nx][ny]='0'
    aptlist.append(count)

for i in range(n):
    for j in range(n):
        if apt[i][j]=='1':
            q=deque()
            q.append((i, j))
            bfs()
            
print(len(aptlist))
aptlist.sort()
for num in aptlist:
    print(num)
    
# 이건 왜 안될까...?
"""
from collections import deque
import sys

n=int(sys.stdin.readline().strip())

apt=[list(sys.stdin.readline().strip()) for _ in range(n)]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
aptlist=[]

for i in range(n):
    for j in range(n):
        if apt[i][j]=='1':
            q=deque()
            q.append((i, j))
            # 시작점 방문처리 잊지않기!
            count=1
            while q:
                x, y=q.popleft()
                apt[x][y]='0'
                for i in range(4):
                    nx=x+dx[i]
                    ny=y+dy[i]
                    if 0<=nx<n and 0<=ny<n and apt[nx][ny]=='1':
                        q.append((nx, ny))
                        count+=1
                        apt[nx][ny]='0'
            aptlist.append(count)

print(len(aptlist))
aptlist.sort()
for num in aptlist:
    print(num)
"""