from collections import deque

m, n=map(int, input().split())
tomato=[]

for _ in range(n):
    tomato.append(list(map(int, input().split())))
    
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
 
def bfs(graph, a, b):
    queue=deque()
    queue.append((a, b))
    days=0
    while queue:
        x, y=queue.popleft()
        if tomato[x][y]==0:
            tomato[x][y]=1
            days+=1
        
        adjCount=0
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if tomato[nx][ny]==0:
                queue.append((nx, ny))
                tomato[nx][ny]=1
                adjCount+=1 
        if adjCount!=0:
            days+=1
    return days

print(bfs(tomato, 0, 0))