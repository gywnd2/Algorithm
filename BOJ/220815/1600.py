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
visited=[[10000]*w for _ in range(h)]
q.append((0,0,0))
visited[0][0]=0

def bfs():
    while q:
        x, y, mov=q.popleft()
        # print("k 이동횟수 :", mov)
        if x==h-1 and y==w-1:
            print(visited[x][y])
            return
        if mov<k:
            # print("체스 말처럼 이동")
            for i in range(8):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<h and 0<=ny<w and visited[nx][ny]==10000 and board[nx][ny]==0:
                    q.append((nx, ny, mov+1))
                    visited[nx][ny]=min(visited[x][y]+1, visited[nx][ny])
        for i in range(4):
            nx=x+dx2[i]
            ny=y+dy2[i]
            if 0<=nx<h and 0<=ny<w and visited[nx][ny]==10000 and board[nx][ny]==0:
                q.append((nx, ny, k))
                visited[nx][ny]=min(visited[x][y]+1, visited[nx][ny])
        # for row in visited:
        #     print(row)
        # print()
    print(-1)

bfs()