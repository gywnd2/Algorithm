from collections import deque
import sys

n=int(sys.stdin.readline().strip())
count=1
area=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

dx, dy=[-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(count):
    while q:
        x, y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and area[nx][ny]==1:
                    q.append((nx, ny))
                    area[nx][ny]=count
                    visited[nx][ny]=1
                    
def visit(ground):
    dist=[[-1 for _ in range(n)] for _ in range(n)]
    global ans
    q=deque()
    
    for x in range(n):
        for y in range(n):
            if area[x][y]==ground:
                q.append((x, y))
                dist[x][y]=0
    while q:
        x, y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and area[nx][ny]>0 and area[nx][ny]!=ground:
                ans=min(ans, dist[x][y])
                return
            if 0<=nx<n and 0<=ny<n and area[nx][ny]==0 and dist[nx][ny]==-1:
                q.append((nx, ny))
                dist[nx][ny]=dist[x][y]+1

visited=[[0 for _ in range(n)] for _ in range(n)]
for x in range(n):
    for y in range(n):
        if area[x][y]==1 and visited[x][y]==0:
            q=deque()
            q.append((x, y))
            area[x][y]=count
            visited[x][y]=1
            bfs(count)
            count+=1

ans=sys.maxsize
for i in range(1, count):
    visit(i)
            
print(ans)