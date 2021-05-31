from collections import deque

def bfs(graph, start, visited):
    # deque 라이브러리를 이용해 큐 생성
    queue=deque([start])
    # 시작 노드 방문처리
    visited[start]=True
    # 큐가 다 비워질 때 까지 수행
    while queue:
        # 큐에서 하나 뽑아 출력
        v=queue.popleft()
        print(v, end='')
        # 방문 했던 노드가 아니라면
        # 인접한 노드를 모두 큐에 삽입하고
        # 방문 노드를 방문 처리
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

graph=[
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3 ,4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited=[False]*9
bfs(graph, 1, visited)