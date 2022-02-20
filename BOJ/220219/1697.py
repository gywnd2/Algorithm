from collections import deque
n, k=map(int, input().split())
dist=[0 for _ in range(100001)]
queue=deque()
queue.append(n)
def bfs():
    while queue:
        loc=queue.popleft()
        if loc==k:
            return dist[k]
        
        for j in (loc-1, loc+1, loc*2):
            if 0<=j<=100000 and dist[j]==0:
                dist[j]=dist[loc]+1
                queue.append(j)

print(bfs())