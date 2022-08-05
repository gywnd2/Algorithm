from collections import deque
import sys

dx, dy=[1, -1, 0, 0], [0, 0, 1, -1]

n, m=map(int, sys.stdin.readline().strip().split())
area=[]
visited=[[[0]*2 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    area.append(list(sys.stdin.readline().strip()))

def bfs():
    while q:
        x, y, wall=q.popleft()
        if x==n-1 and y==m-1:
            print(visited[x][y][wall])
            return
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny][wall]==0:
                if area[nx][ny]=='0':
                    q.append((nx, ny, wall))
                    visited[nx][ny][wall]=visited[x][y][wall]+1
                if wall==0 and area[nx][ny]=='1':
                    q.append((nx, ny, 1))
                    visited[nx][ny][1]=visited[x][y][wall]+1
    print(-1)
                                
q=deque()
q.append((0,0,0))
visited[0][0][0]=1
bfs()