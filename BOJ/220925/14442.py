import sys
from collections import deque
q=deque()
def bfs():
    while q:
        x, y, wall=q.popleft()
        if x==n-1 and y==m-1:
            return min(visited[x][y])
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # print('nx :',nx,'ny :',ny,'wall :', wall)
            # print('visited[x][y][wall]=',visited[x][y][wall])
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny]=='0' and visited[nx][ny][wall]==sys.maxsize:
                    q.append((nx, ny, wall))
                    visited[nx][ny][wall]=visited[x][y][wall]+1
                    # print('visited[nx][ny][wall] :',visited[nx][ny][wall], 'visited[nx][ny][wall]+1 :', visited[nx][ny][wall]+1)
                elif wall<k and board[nx][ny]=='1' and visited[nx][ny][wall]==sys.maxsize:
                    q.append((nx, ny, wall+1))
                    visited[nx][ny][wall+1]=visited[x][y][wall]+1
                    # print('visited[nx][ny][wall+1] :',visited[nx][ny][wall+1], 'visited[nx][ny][wall]+1 :', visited[nx][ny][wall]+1)
    return -1
                
                

dx, dy=[1, -1, 0, 0], [0, 0, 1, -1]
n, m, k=map(int, sys.stdin.readline().strip().split())
visited=[[[sys.maxsize for _ in range(k+1)] for _ in range(m)] for _ in range(n)]

board=[list(sys.stdin.readline().strip()) for _ in range(n)]
q.append((0,0,0))
visited[0][0][0]=1
print(bfs())