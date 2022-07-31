from collections import deque
import sys

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

m, n, k = map(int, sys.stdin.readline().strip().split())

# 모눈종이 왼쪽 아래 = 0,0
# 오른쪽 위 = N, M
area=[[0 for _ in range(n)] for _ in range(m)]
areaSize=[]
for _ in range(k):
    lx, ly, rx, ry= map(int, sys.stdin.readline().strip().split())
    for i in range(ly, ry):
        for j in range(lx, rx):
            area[i][j]=1

for row in range(m):
    for column in range(n):
        if area[row][column]==0:
            size=1
            # 큐를 빈 공간 찾을 때마다 초기화 해야함
            q=deque()
            q.append((row, column))
            while q:
                x, y=q.popleft()
                area[x][y]=1
                for i in range(4):
                    nx=x+dx[i]
                    ny=y+dy[i]
                    if 0<=nx<m and 0<=ny<n and area[nx][ny]==0:
                        q.append((nx, ny))
                        size+=1
                        area[nx][ny]=1
            areaSize.append(size)
            
print(len(areaSize))
areaSize.sort()
for num in areaSize:
    print(num, end=' ')