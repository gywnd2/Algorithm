import sys, copy

n, m=map(int, sys.stdin.readline().strip().split())
office=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
dx, dy=[-1, 1, 0, 0], [0, 0, -1, 1]
# 0 : 상, 1 : 하, 2 : 좌, 3 : 우 
direction=[[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 3], [1, 3], [1, 2], [0, 2]],
           [[0, 2, 3], [0, 1, 3], [1, 2, 3], [0, 1, 2]], [[0, 1, 2, 3]]]
cctv=[]
cctvCount=0
ans=sys.maxsize


def watch(x, y, direction, tmp):
    for d in direction:
        nx, ny=x, y
        while True:
            nx+=dx[d]
            ny+=dy[d]
            
            if 0<=nx<n and 0<=ny<m and tmp[nx][ny] != 6:
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = '#'
            else:
                break
            
            # 이렇게 하면 0이 아니면 그냥 break 되어버림
            # 0이 아니지만 더 탐색할 수 있는 경우(6이 아닌 나머지인 경우)를 고려해야함
            # if 0<=nx<n and 0<=ny<m and tmp[nx][ny]==0:
            #         tmp[nx][ny] = '#'
            # else:
            #     break
            
def dfs(cnt, data):
    global ans
    tmp=copy.deepcopy(data)
    
    if cctvCount==cnt:
        count=0
        for t in tmp:
            count+=t.count(0)
        ans=min(ans, count)
        return
    
    x, y, c=cctv[cnt]
    for d in direction[c]:
        watch(x, y, d, tmp)
        dfs(cnt+1, tmp)
        tmp=copy.deepcopy(data)
            
for x in range(n):
    for y in range(m):
        if office[x][y] !=0 and office[x][y]!=6:
            cctvCount+=1
            cctv.append((x, y, office[x][y]))
            
dfs(0, office)
print(ans)