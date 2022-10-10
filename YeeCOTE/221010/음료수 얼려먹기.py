import sys
from collections import deque

dx, dy=[-1, 1, 0, 0], [0, 0, -1, 1]
q=deque()
count=0

n, m=map(int, sys.stdin.readline().strip().split())
ice=[list(sys.stdin.readline().strip()) for _ in range(n)]
visited=[[False for _ in range(m)] for _ in range(n)]

def bfs():
    while q:
        x, y=q.popleft()
        for i in range(4):
            nx=x+dx[i]; ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and ice[nx][ny]=='0':
                q.append((nx, ny))
                visited[nx][ny]=True

for i in range(n):
    for j in range(m):
        if ice[i][j]=='0' and not visited[i][j]:
            count+=1
            q.append((i, j))
            visited[i][j]=True
            bfs()
            
print(count)