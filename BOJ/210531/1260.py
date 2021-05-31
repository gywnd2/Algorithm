from collections import deque
import sys
def bfs(graph, start, visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

def dfs(graph, v, visited):
    visited[v]=True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

N, M, V=map(int, sys.stdin.readline().strip().split())
input=list(tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(M))
graph=[[] for _ in range(N+1)]
for edge in input:
    graph[edge[0]].append(edge[1])
    graph[edge[0]]=list(set(graph[edge[0]]))
    graph[edge[0]].sort()
    graph[edge[1]].append(edge[0])
    graph[edge[1]]=list(set(graph[edge[1]]))
    graph[edge[1]].sort()
visitedBfs=[False]*(N+1)
visitedDfs=[False]*(N+1)
dfs(graph, V, visitedDfs)
print()
bfs(graph, V, visitedBfs)
