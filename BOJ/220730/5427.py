from collections import deque
import sys

# 하, 상, 좌, 우 순서
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]


def bfs():
    queueH=deque()
    queueF=deque()
    for row in range(h):
        for column in range(w):
            if bldg[row][column]=='@':
                queueH.append((row, column))
            elif bldg[row][column]=='*':
                queueF.append((row, column))
    
    while queueH and queueF:
        xS, yS=queueH.popleft()
        xF, yF=queueF.popleft()
        visited[xF][yF]=1
        for i in range(4):
            nxS=xS+dx[i]; nxF=xF+dx[i]
            nyS=yS+dy[i]; nyF=yF+dy[i]
            # 매초 마다 빈 공간 '.' 으로 불 확산
            # 동서남북으로 이동가능 (1초 소요)
            # 불 붙은 칸, 불이 붙을 예정인 칸으로 이동불가
            # 불이 옮겨옴과 동시에 이동가능
            
            # 불 먼저 계산
            if 0<=nxF<h and 0<=nyF<w and bldg[nxF][nyF] not in {'*', '#'}:
                queueF.append((nxF, nyF))
                visited[nxF][nyF]=1
                bldg[nxF][nyF]='*'
            
            # 상근 계산
            if 0<=nxS<h and 0<=nyS<w and bldg[nxS][nyS]=='.' and visited[nxS][nyS]==0:
                queueH.append((nxS, nyS))
                time[nxS][nyS]=time[xS][yS]+1
                bldg[nxS][nyS]='@'
                    
            elif ((nxS>=h or nxS<0) and 0<=nyS<w) or ((nyS>=w or nyS<0) and 0<=nxS<h):
                print(time[xS][yS]+1)
                return
                
    print("IMPOSSIBLE")
    return
                
t=int(sys.stdin.readline().strip())

for _ in range(t):
    w, h=map(int, sys.stdin.readline().strip().split())
    bldg=[list(sys.stdin.readline().strip()) for _ in range(h)]
    visited=[[0 for _ in range(w)] for _ in range(h)]
    time=[[0 for _ in range(w)] for _ in range(h)]
    bfs()