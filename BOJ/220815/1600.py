from collections import deque
import sys

k=int(sys.stdin.readline().strip())
w, h=map(int, sys.stdin.readline().strip().split())
board=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(h)]

dx=[-2, -1, 1, 2, -2, -1, 1, 2]
dy=[1, 2, 2, 1, -1, -2, -2, -1]
dx2=[-1, 1, 0, 0]
dy2=[0, 0, -1, 1]

q=deque()
visited=[[[sys.maxsize for _ in range(k)] for _ in range(w)] for _ in range(h)]
q.append((0,0,0))
visited[0][0][0]=0

def bfs():
    while q:
        x, y, mov=q.popleft()
        if x==h-1 and y==w-1:
            print(min(visited[x][y]))
            return
        if mov<k:
            for i in range(8):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<h and 0<=ny<w and visited[nx][ny][mov]==sys.maxsize and board[nx][ny]==0:
                    q.append((nx, ny, mov+1))
                    visited[nx][ny][mov]=min(visited[x][y][mov]+1, visited[nx][ny][mov])
        for i in range(4):
            nx=x+dx2[i]
            ny=y+dy2[i]
            if 0<=nx<h and 0<=ny<w and visited[nx][ny][k-1]==sys.maxsize and board[nx][ny]==0:
                q.append((nx, ny, k))
                visited[nx][ny][k-1]=min(visited[x][y][k-1]+1, visited[nx][ny][k-1])
    print(-1)

bfs()