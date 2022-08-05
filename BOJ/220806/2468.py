from collections import deque
import sys

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def bfs():
    while q:
        x, y=q.popleft()
        visited[x][y]=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and area[nx][ny]>th and visited[nx][ny]==0:
                q.append((nx, ny))
                visited[nx][ny]=1
                
safe=[]
n=int(sys.stdin.readline().strip())
area=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
maxThreshold=max(map(max, area))

for th in range(maxThreshold):
    visited=[[0 for _ in range(n)] for _ in range(n)]
    count=0
    for x in range(n):
        for y in range(n):
            if area[x][y]>th and visited[x][y]==0:
                q=deque()
                q.append((x, y))
                bfs()
                count+=1
    safe.append(count)
print(max(safe))