from collections import deque
import sys

n,k=map(int, sys.stdin.readline().strip().split())

# 순간이동이 먼저 수행 되도록 해야함
dx=[0, 1, -1]
q=deque()
visited=[sys.maxsize for _ in range(100001)]
q.append(n)
visited[n]=0
dist=[]

def bfs():
    while q:
        x=q.popleft()
        if x==k:
            print(visited[x])
            return 
        for i in range(3):
            if dx[i]==0:
                nx=x*2
                if 0<=nx<100001 and visited[nx]==sys.maxsize:
                    q.appendleft(nx)
                    visited[nx]=visited[x]
            else:
                nx=x+dx[i]
                if 0<=nx<100001 and visited[nx]==sys.maxsize:
                    q.append(nx)
                    visited[nx]=visited[x]+1
bfs()