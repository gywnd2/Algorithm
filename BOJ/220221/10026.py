from collections import deque
import copy

n=int(input())
r, g, b, rg=0, 0, 0, 0
color=[list(input()) for _ in range(n)]
colorCopy=copy.deepcopy(color)
dx, dy=[1, -1, 0, 0], [0, 0, 1, -1]

def bfs(a, b, switch):
    queue=deque()
    if color[a][b]==switch:
        queue.append((a, b))
        
    while queue:
        x, y=queue.popleft()
        color[x][y]=0
          
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and color[nx][ny]==switch:
                color[nx][ny]=0
                queue.append((nx, ny))
    return 1

def weakBFS(a, b):
    queue=deque()
    if colorCopy[a][b] in ('R', 'G'):
        queue.append((a, b))
        
    while queue:
        x, y=queue.popleft()
        colorCopy[x][y]=0
          
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and colorCopy[nx][ny] in ('R', 'G'):
                colorCopy[nx][ny]=0
                queue.append((nx, ny))
    return 1

for i in range(n):
    for j in range(n):
        if color[i][j]=='R':
            r+=bfs(i, j, 'R')
        elif color[i][j]=='G':
            g+=bfs(i, j, 'G')
        elif color[i][j]=='B':
            b+=bfs(i, j, 'B')

for i in range(n):
    for j in range(n):
        if colorCopy[i][j] in ('R', 'G'):
            rg+=weakBFS(i, j)
            
print(r+g+b, rg+b)