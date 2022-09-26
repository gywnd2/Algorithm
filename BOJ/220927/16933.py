import sys
from collections import deque

n, m, k=map(int, sys.stdin.readline().strip().split())
board=[list(sys.stdin.readline().strip()) for _ in range(n)]
visited=[[[sys.maxsize for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
#하상우좌
dx, dy=[1, -1, 0, 0], [0, 0, 1, -1]
q=deque()
def bfs():
    isDay=True
    while q:
        # print("isday :",isDay)
        x, y, wall=q.popleft()
        if x==n-1 and y==m-1:
            return min(visited[x][y])
        # 안움직이는 경우는 한번만 세도록
        isMoved=False
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if wall<k and visited[nx][ny][wall+1]==sys.maxsize and board[nx][ny]=='1' and isDay:
                    q.append((nx, ny, wall+1))
                    visited[nx][ny][wall+1]=visited[x][y][wall]+1
                    isMoved=True
                elif visited[nx][ny][wall]==sys.maxsize and board[nx][ny]=='0':
                    q.append((nx, ny, wall))
                    visited[nx][ny][wall]=visited[x][y][wall]+1
                    isMoved=True
                # 밤이라 벽을 못 부순다
                elif wall<k and visited[nx][ny][wall]==sys.maxsize and board[nx][ny]=='1' and not isDay and not isMoved:
                    q.append((x, y, wall))
                    visited[x][y][wall]+=1
        isDay=not isDay
                    
    return -1
                    
q.append((0,0,0))
visited[0][0][0]=1
print(bfs())