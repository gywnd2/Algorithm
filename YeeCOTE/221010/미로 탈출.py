import sys
from collections import deque

n, m=map(int, sys.stdin.readline().strip().split())
maze=[list(sys.stdin.readline().strip()) for _ in range(n)]
visited=[[sys.maxsize for _ in range(m)] for _ in range(n)]
dx, dy=[0, -1, 1, 0], [1, 0, 0, -1]
q=deque()
count=0

def bfs():
    while q:
        x, y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==sys.maxsize and maze[nx][ny]=='1':
                q.append((nx, ny))
                visited[nx][ny]=min(visited[nx][ny], visited[x][y]+1)
    
q.append((0, 0))
visited[0][0]=1
bfs()
print(visited[n-1][m-1])