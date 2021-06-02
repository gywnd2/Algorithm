################
# 이것이 코딩 테스트다 Chap.4
# 3. 게임개발
# 0 : 육지 / 1 : 바다
# 처음 위치는 항상 육지
# 갈 방향은 왼쪽 부터 선택 (반시계 90도 회전 방향)
# 왼쪽에 가지 않은칸이 존재    -> 왼쪽으로 회전 하고 한칸 전진
#                      없다면  -> 왼쪽으로 회전 하고 1단계로
# 네 방향 모두 가본 칸 or 바다 -> 방향유지 & 한칸 뒤로 하고 1단계로
#               or 뒤에도 바다 -> End
# d : 북 동 남 서 -> 0 1 2 3
################
import sys
N, M=map(int, sys.stdin.readline().strip().split())
A, B, d=map(int, sys.stdin.readline().strip().split())
visited=[[False]*N for _ in range(M)]
visited[A][B]=True
world=list(list(map(int, sys.stdin.readline().strip().split())) for _ in range(M))
directionX=[0, 1, 0, -1]; directionY=[-1, 0, 1, 0]
count=1; turn_time=0

def turn_left():
    global direction
    direction-=1
    if direction==-1:
        direction=3

while True:
    turn_left()
    nx=x+directionX[d]
    ny=y+directionY[d]
    if d[nx][ny]==0 and world[nx][ny]:
        d[nx][ny]=1
        x=nx; y=ny; count+=1
        turn_time=0
        continue
    else:
        turn_time+=1
    if turn_time==4:
        nx=x-directionX[d]
        ny=y-directionY[d]
        if array[nx][ny]==0:
            x=nx; y=ny
        else: break
        turn_time=0
print(count)