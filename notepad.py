from collections import deque
def bfs(graph, start, visited):
    # Assign queue variable using deque library
    queue=deque([start])
    # Check start node as visited
    visited[start]=True
    # Run until queue is empty
    while queue:
        # Pop a node from left
        v=queue.popleft()
        # Print value
        print(v,end=' ')
        # Add adjacent nodes from start node 'v'
        # to destination node 'i'
        # and check visited 'True'
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

def dfs(graph, v, visited):
    # Check start node as visited
    visited[v]=True
    # Print value of node
    print(v, end=' ')
    # If adjacent node is not visited,
    # call dfs recursively
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

visited=[False]*(N+1)

# Numbers of vertices and edges are N, M respectively
N, M=map(int, input().split())
# Input edges as list of tuples
input=list(tuple(map(int, input().split())) for _ in range(M))
# Initialize empty 2-D list as temporary graph to assign edges
graph=[[] for _ in range(N+1)]
# For each edge
for edge in input:
    # Use index of 'graph' to match with start node of edge
    # So leave index #0 empty
    # And value of each index is destination node of edge
    # If edge=(0, 5) => graph[edge[0]]=edge[1]
    # => [0,5]
    graph[edge[0]].append(edge[1])
    # Remove repeated edge
    graph[edge[0]]=list(set(graph[edge[0]]))
    # Sort in ascending order
    graph[edge[0]].sort()
    # Same process, just reversed order of edge
    graph[edge[1]].append(edge[0])
    graph[edge[1]]=list(set(graph[edge[1]]))
    graph[edge[1]].sort()

visitedBfs=[False]*(N+1)
visitedDfs=[False]*(N+1)
dfs(graph, V, visitedDfs)
print()
bfs(graph, V, visitedBfs)
