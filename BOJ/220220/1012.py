import sys
from collections import deque

t=int(sys.stdin.readline().strip())
    
def bfs(a, b):
    fQueue=deque()
    fQueue.append((a, b))
    field[a][b]=0
    while fQueue:
        x, y=fQueue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # 좌표 범위 확인 시 가로길이, 세로길이 등 용어의 의미를 정확히 파악할 것
            if 0<=nx<n and 0<=ny<m and field[nx][ny]==1:
                field[nx][ny]=0
                fQueue.append((nx, ny))
    return 1

for _ in range(t):
    # 가로길이 m, 세로 길이 n, 배추 개수 k
    # 가로길이 -> Column, 세로길이 -> Row / 구분을 잘하자!
    m, n, k=map(int, sys.stdin.readline().strip().split())
    field=[[0 for _ in range(m)] for _ in range(n)]
    dx, dy=[1, -1, 0, 0], [0, 0, 1, -1]
    count=0
    
    for _ in range(k):
        column, row=map(int, sys.stdin.readline().strip().split())
        field[row][column]=1
    
    for i in range(n):
        for j in range(m):
            if field[i][j]==1:
                count+=bfs(i, j)
                
    print(count)