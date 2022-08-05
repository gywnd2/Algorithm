from collections import deque
import sys

dx=[-1, 1, 0, 0, 0, 0]
dy=[0, 0, -1, 1, 0, 0]
dz=[0, 0, 0, 0, -1, 1]

def bfs():
    while q:
        z, x, y=q.popleft()
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            if 0<=nx<r and 0<=ny<c and 0<=nz<l and visited[nz][nx][ny]==0:
                if building[nz][nx][ny]=='E':
                    print("Escaped in "+str(visited[z][x][y])+" minute(s).")
                    return
                elif building[nz][nx][ny]=='.':
                    visited[nz][nx][ny]=visited[z][x][y]+1
                    q.append((nz, nx, ny))
    print("Trapped!")
    
while True:
    l,r,c=map(int, sys.stdin.readline().strip().split())
    if l==0 and r==0 and c==0:
        break
    
    building=[]
    q=deque()
    visited=[[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]
    for _ in range(l):
        tmp=[]
        for _ in range(r):
            tmp.append(list(sys.stdin.readline().strip()))
        building.append(tmp)
        sys.stdin.readline()
    
    for f in range(l):    
        for x in range(r):
            for y in range(c):
                if building[f][x][y]=='S' and visited[f][x][y]==0:
                    q.append((f, x, y))
                    visited[f][x][y]=1
                    bfs()
                    break