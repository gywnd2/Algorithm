import sys
from collections import deque

n, m, k=map(int, sys.stdin.readline().strip().split())
board=[list(sys.stdin.readline().strip()) for _ in range(n)]
visited=[[[False for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
#하상우좌
dx, dy=[-1, 1, 0, 0], [0, 0, 1, -1]
q=deque()
def bfs():
    isDay=True
    distance=1
    while q:
        for _ in range(len(q)):
            x, y, wall, dist=q.popleft()
            if x==n-1 and y==m-1:
                return dist
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if wall<k and visited[nx][ny][wall+1]==False and board[nx][ny]=='1':
                        if isDay:
                            q.append((nx, ny, wall+1, distance+1))
                            visited[nx][ny][wall+1]=True
                        else:
                            q.append((x, y, wall, distance+1))
                    elif visited[nx][ny][wall]==False and board[nx][ny]=='0':
                        q.append((nx, ny, wall, distance+1))
                        visited[nx][ny][wall]=True
        isDay=not isDay
        distance+=1
    return -1
                    
q.append((0,0,0,1))
visited[0][0][0]=True
print(bfs())