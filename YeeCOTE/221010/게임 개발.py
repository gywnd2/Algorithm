import sys
from collections import deque
n, m=map(int, sys.stdin.readline().strip().split())
a, b, d=map(int, sys.stdin.readline().strip().split())
world=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]
visited=[[False for _ in range(m)] for _ in range(n)]
dx, dy=[-1, 0, 1, 0], [0, 1, 0, -1]
q=deque()
q.append((a, b, d))
visited[a][b]=True
count=0
def bfs():
    global count
    while q:
        x, y, dir=q.popleft()
        count+=1
        dirIdx=0
        while True:
            if dirIdx>3:
                break
            ndir=(dir+dirIdx)%4
            nx=x+dx[ndir]
            ny=y+dy[ndir]
            # 범위 내에서
            if 0<=nx<n and 0<=ny<m:
                # 가보지 않은 육지는 왼쪽으로 전진
                if not visited[nx][ny] and world[nx][ny]==0:
                    q.append((nx, ny, ndir))
                    visited[nx][ny]=True
                    break
                # 바다거나 가봤다면 방향만 전환
                elif visited[nx][ny] or world[nx][ny]==1:
                    ndir=(ndir+1)%4
                    dirIdx+=1
                # 네 방향 모두 갈 곳이 없거나 바다인 경우 방향 유지하고 한칸 뒤로 하고 다시 1단계
                elif dirIdx==3 and (world[nx][ny]==1 or visited[nx][ny]):
                    q.append((x, y, ndir))
            # 범위를 벗어났을 경우 방향만 전환:
            else:
                dirIdx+=1
bfs()
print(count)