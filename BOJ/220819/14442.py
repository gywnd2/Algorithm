from collections import deque
import sys

n, m, k=map(int, sys.stdin.readline().strip().split())
board=[list(sys.stdin.readline().strip()) for _ in range(n)]

dx, dy=[-1, 1, 0, 0], [0, 0, -1, 1]

def bfs():
    q=deque()
    q.append((0,0,0))
    visited=[[[0]*(k+1) for _ in range(m)] for _ in range(n)]
    while q:
        x, y, wall=q.popleft()
        if x==n-1 and y==m-1:
            print(visited[x][y][wall]+1)
            return
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny][wall]==0:
                if wall<k and board[nx][ny]=='1':
                # board의 데이터 타입(str? int?) 꼭 확인!!!!!!!!
                    visited[nx][ny][wall+1]=visited[x][y][wall]+1
                    q.append((nx, ny, wall+1))
                if board[nx][ny]=='0':
                    visited[nx][ny][wall]=visited[x][y][wall]+1
                    q.append((nx, ny, wall))
    print(-1)
    return
                
bfs()