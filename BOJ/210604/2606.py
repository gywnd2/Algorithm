computers=int(input())
pairs=int(input())
connections=[[] for _ in range(101)]
for _ in range(pairs):
    a, b=map(int, input().split())
    connections[a].append(b)
    connections[b].append(a)
    connections[a]=list(set(connections[a]))
    connections[b]=list(set(connections[b]))
visited=[False for _ in range(computers+1)]
count=0
def dfs(graph, v, visited):
    global count
    visited[v]=True
    if v!=1:
        count+=1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(connections, 1, visited)
print(count)