import sys, copy
from collections import deque
from itertools import combinations

input=sys.stdin.readline
N, M=map(int, input().strip().split())
lab=[list(map(int, input().strip().split())) for _ in range(N)]
wall, virus=[], []
dx, dy=[1, -1, 0, 0], [0, 0, 1, -1]
q=deque()


def bfs(check):
    # print("q:",q)
    count=0
    while q:
        x, y=q.popleft()
        count+=1
        visited[x][y]=True
        tmpLab[x][y]=check
        for i in range(4):
            nx, ny=x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and tmpLab[nx][ny]==0:
                visited[nx][ny]=True
                q.append((nx, ny))
    return count

for i in range(N):
    for j in range(M):
        if lab[i][j]==0:
            wall.append((i, j))
        elif lab[i][j]==2:
            virus.append((i, j))

wallCandidate=list(combinations(wall, 3))
maxArea=0

for comb in wallCandidate:
    visited=[[False]*M for _ in range(N)]
    # print("comb :",comb)
    tmpLab=copy.deepcopy(lab)
    for w in comb:
        tmpLab[w[0]][w[1]]=1
    q.extend(virus)
    bfs(2)
    
    # print("after virus")
    # for r in tmpLab:
    #     print(r)
        
    visited=[[False]*M for _ in range(N)]
    tmpArea=0    
    for i in range(N):
        for j in range(M):
            if tmpLab[i][j]==0:
                q.append((i,j))
                tmpArea+=bfs(3)
    maxArea=max(maxArea, tmpArea)
    # print("tmpArea : ",tmpArea)
    # for r in tmpLab:
    #     print(r)
print(maxArea)
            