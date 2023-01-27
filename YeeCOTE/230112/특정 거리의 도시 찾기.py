from collections import deque
import sys

N, M, K, X=map(int, sys.stdin.readline().strip().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    A, B=map(int, sys.stdin.readline().strip().split())
    graph[A].append(B)

q=[]
answer=[]
visited=[sys.maxsize for _ in range(N+1)]

def dfs(start):
    q.append(start)
    visited[start]=0
    while q:
        cur=q.pop()
        for dest in graph[cur]:
            if visited[dest]>visited[cur]+1:
                # q.append(dest)
                visited[dest]=min(visited[dest], visited[cur]+1)
                q.append(dest)

dfs(X)

for i in range(N+1):
    if visited[i]==K:
        answer.append(i)

if len(answer)==0:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)