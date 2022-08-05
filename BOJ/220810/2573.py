from collections import deque
import sys

dx, dy=[-1, 1, 0, 0], [0, 0, -1, 1]

def melt(x, y):
    meltCount=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and ice[nx][ny]<=0:
            meltCount+=1
    meltQ.append((x,y,meltCount))
            
def bfs():
    size=1
    while q:
        x, y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and ice[nx][ny]>0:
                q.append((nx, ny))
                visited[nx][ny]=1
                size+=1
    area.append(size)
                
n, m=map(int, sys.stdin.readline().strip().split())
ice=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
area=[]
count=0

while True:
    # 빙하의 합이 0 (모두 녹을 까지 분리 X)
    # tmp=0
    # for row in ice:
    #     tmp+=sum(row)
    # if tmp==0:
    #     print(0)
    #     break
    
    # 녹는 빙하 계산
    meltQ=deque()
    for x in range(n):
        for y in range(m):
            if ice[x][y]>0:
                melt(x, y)
    if len(meltQ)==0:
        print(0)
        break
    while meltQ:
        x, y, meltCount=meltQ.popleft()
        if ice[x][y]-meltCount<0:
            ice[x][y]=0
        else:
            ice[x][y]-=meltCount
    
    # 1년 경과
    count+=1
    
    # 빙하 영역 계산
    q=deque()
    visited=[[0 for _ in range(m)] for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if ice[x][y]>0 and visited[x][y]==0:
                q.append((x,y))
                visited[x][y]=1
                bfs()
                
    # 만약 영역의 개수가 2이상이면 탈출
    if len(area)>=2:
        print(count)
        break     
    else:
        # print("빙하가 분리되지 않아 초기화")
        area=[]
        continue
    