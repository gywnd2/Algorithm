def dfs(graph, v, visited):
    # 노드를 방문처리하고 출력
    visited[v]=True
    print(v, end='')
    # 각 노드와 인접한 노드를 전부 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i , visited)

# 각 노드와 그 인접한 노드를 작은 순으로 입력
graph=[
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 모든 노드의 방문여부는 False에서 시작ㄴ
visited=[False]*9 
dfs(graph, 1, visited)