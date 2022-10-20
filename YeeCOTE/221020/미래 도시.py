import sys, heapq
n, m=map(int, sys.stdin.readline().strip().split())
graph=[[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    start, dest=map(int, sys.stdin.readline().strip().split())
    graph[start][dest]=1
    graph[dest][start]=1

x, k=map(int, sys.stdin.readline().strip().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])

res=graph[1][k]+graph[k][x]
if res>=sys.maxsize:
    print(-1)
else:
    print(res)