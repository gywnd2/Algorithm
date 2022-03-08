import sys
from collections import deque
m, n, h=map(int, sys.stdin.readline().strip().split())
result=0
tomatoes=[list(list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)) for _ in range(h)]
queue=deque()
dx, dy, dz=[1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]

def bfs():
    while queue:
        x, y, z=queue.popleft()
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            if 0<=nx<n and 0<=ny<m and 0<=nz<h and tomatoes[nz][nx][ny]==0:
                tomatoes[nz][nx][ny]=tomatoes[z][x][y]+1
                queue.append((nx, ny, nz))
            
for layer in range(h):
    for row in range(n):
        for column in range(m):
            if tomatoes[layer][row][column]==1:
                queue.append((row, column, layer))
                
bfs()
for layer in tomatoes:
    for row in layer:
        for column in row:
            if column==0:
                print(-1)
                exit(0)
        # result=max(result, max(row))-1
        # 위와 같이 -1을 해준 것으로 max 연산을 하게되면
        # 오차가 발생하게 된다.
        result=max(result, max(row))

print(result-1)