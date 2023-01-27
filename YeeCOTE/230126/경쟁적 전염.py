import sys
from collections import deque

input=sys.stdin.readline
N,K=map(int, input().strip().split())
test=[list(map(int, input().strip().split())) for _ in range(N)]
S,X,Y=map(int, input().strip().split())
dx, dy=[1, -1, 0, 0], [0, 0, 1, -1]
viruses=[] 
def bfs(v):
    q=deque(v)
    count=0
    while q:
        if count==S:
            break
        for _ in range(len(q)):
            virus, x, y=q.popleft()
            for j in range(4):
                nx=x+dx[j]; ny=y+dy[j]
                if 0<=nx<N and 0<=ny<N and test[nx][ny]==0:
                    test[nx][ny]=virus
                    q.append((virus, nx, ny))
        count+=1
    # for r in test:
    #     print(r)
    # print("!!!!")

               
for i in range(N):
    for j in range(N):
        if test[i][j]!=0:
            viruses.append((test[i][j],i, j))
viruses.sort()
bfs(viruses)
print(test[X-1][Y-1])