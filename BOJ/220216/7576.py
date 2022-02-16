from collections import deque

m, n=map(int, input().split())
tomato=[]
res=0

for _ in range(n):
    tomato.append(list(map(int, input().split())))
    
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
queue=deque([])

for i in range(n):
    for j in range(m):
        if tomato[i][j]==1:
            queue.append((i,j))
 
def bfs():
    while queue:
        x, y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and tomato[nx][ny]==0:
                tomato[nx][ny] = tomato[x][y]+1
                queue.append((nx, ny))

bfs()
for i in tomato:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    res=max(res, max(i))
print(res-1)