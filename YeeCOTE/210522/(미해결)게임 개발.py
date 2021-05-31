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
A, B, d=map(int, input().split())
visited=[[0]*N for _ in range[M]]
world=list(list(map(int, sys.stdin.readline().strip().split())) for _ in range(M))
count=0
directionX=[-1, 0, 1, 0]; directionY=[0, 1, 0, -1]
def left():