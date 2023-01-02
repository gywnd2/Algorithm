import heapq

N, M=map(int, input().split())

graph=[[int(1e9) for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b=map(int, input().split())
    graph[a][b]=1
    graph[b][a]=1

for a in range(N+1):
    for b in range(N+1):
        if a==b:
            graph[a][b]=0
    
X, K=map(int,input().split())

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])

if graph[1][K]+graph[K][X]>=int(1e9):
    print(-1)
else:
    print(graph[1][K]+graph[K][X])