import sys
from collections import deque
t=int(sys.stdin.readline().strip())
dx=[1, 1, 2, 2, -1, -1, -2, -2]
dy=[2, -2, 1, -1, 2, -2, 1, -1]

def bfs():
    queue=deque()
    queue.append(curPos)
    while queue:
        x, y=queue.popleft()
        if x==destPos[0] and y==destPos[1]:
            print(chess[x][y]-1)
            return
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<l and 0<=ny<l and chess[nx][ny]==0:
                chess[nx][ny]=chess[x][y]+1
                queue.append((nx, ny))
    
for _ in range(t):
    l=int(sys.stdin.readline().strip())    
    chess=[[0 for _ in range(l)] for _ in range(l)]
    curPos=list(map(int, sys.stdin.readline().strip().split()))
    chess[curPos[0]][curPos[1]]=1
    destPos=list(map(int, sys.stdin.readline().strip().split()))
    bfs()