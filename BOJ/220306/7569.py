from collections import deque
m, n, h=map(int, input().split())
result=0; tmp=0
tomatoes=[list(list(map(int, input().split())) for _ in range(n)) for _ in range(h)]
queue=deque()
dx, dy=[1, -1, 0, 0], [0, 0, 1, -1]

def bfs(plate):
    while queue:
        x, y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and plate[nx][ny]==0:
                plate[nx][ny]=1
                queue.append((nx, ny))
   
if h>1:
    switch=False             
    for i in range(h):
        for row in range(n):
            for column in range(m):
                if tomatoes[i][row][column]==1:
                    queue.append(tomatoes[i][row][column])
        bfs(tomatoes[i])
        for j in tomatoes[i]:
            if switch:
                break
            for h in j:
                if h==0:
                    switch=True
            tmp=max(tmp, max(i))-1
        result+=tmp
else:
    bfs(tomatoes)
    for i in tomatoes:
        for j in i:
            if j==0:
                print(-1)
                exit(0)
        tmp=max(tmp, max(i))-1
    result+=tmp

if result==h:
    print(max(res))