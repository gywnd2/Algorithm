import sys
from collections import deque

r, c=map(int, sys.stdin.readline().strip().split())
maze=[list(input()) for _ in range(r)]
hQueue, fQueue=deque(), deque()
dx, dy=[1, 0, -1, 0], [0, 1, 0, -1]
hGraph, fGraph=[[0]*c for _ in range(r)], [[0]*c for _ in range(r)]

# 지훈이와 불 위치 확인
for i in range(r):
    for j in range(c):
        if maze[i][j]=='F':
            fQueue.append((i, j))
            
        elif maze[i][j]=='J':
            hQueue.append((i, j))

def bfs():
    # 불에 대해 BFS
    while fQueue:
        x, y=fQueue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # 좌표를 벗어나지 않았고 / 벽이 아니고 / 불이 아직 번지지 않음 == 불이 나야할 곳
            if 0<=nx<r and 0<=ny<c:
                if maze[nx][ny]!='#' and fGraph[nx][ny]==0:
                    fGraph[nx][ny]=fGraph[x][y]+1
                    fQueue.append((nx, ny))
                
    # 지훈이 BFS
    while hQueue:
        x, y=hQueue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # 좌표 안 벗어남 == 아직 탈출 못함
            if 0<=nx<r and 0<=ny<c:
                # 벽이 아니고 / 불이 나지 않았거나 / 아직 가지 않은 곳 == 이동할 수 있는곳
                # 불이 번지는 데 걸린 시간 보다 먼저 도달할 수 있는 곳
                # --> 이동할 수 있는 곳
                if maze[nx][ny]!='#' and hGraph[nx][ny]==0:
                    if fGraph[nx][ny]==0 or fGraph[nx][ny]>hGraph[x][y]+1:
                        hGraph[nx][ny]=hGraph[x][y]+1
                        hQueue.append((nx, ny))
            # 좌표를 벗어남 == 탈출!
            else:
                return hGraph[x][y]+1
            
    # 이동할 수 있는 경우의 수를 모두 시도 했으나 (= 큐가 빔)
    # 좌표를 벗어나지 못함        
    return 'IMPOSSIBLE'               

print(bfs())