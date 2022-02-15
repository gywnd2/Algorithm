from collections import deque

n, m=map(int, input().split())
maze=[]
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

for _ in range(n):
    maze.append(list(input()))

def bfs(graph, a, b):
    queue=deque()
    queue.append((a, b))
    count=1
    
    while queue:
        x, y=queue.popleft()
            
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            elif nx==n-1 and ny==m-1:
                count+=1
                return count
            elif maze[nx][ny]=="1":
                maze[nx][ny]=str(int(maze[x][y])+1)
                print("!!!found!!! :", nx, ny)
                queue.append((nx, ny))
                count+=1

print(bfs(maze, 0, 0))