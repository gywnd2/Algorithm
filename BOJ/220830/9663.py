import sys

n=int(sys.stdin.readline().strip())
board=[[0 for _ in range(n)] for _ in range(n)]
count=0
dx, dy=[1, -1, 0, 0, 1, 1, -1, -1], [0, 0, 1, -1, 1, -1, 1, -1]

def check(x, y):
    if x>=n or y>=n or x<0 or y<0:
        return
    if not board[x][y]:
        print("board[",x,"][",y,"] : ", board[x][y])
        board[x][y]=1
        return True
    elif board[x][y]:
        print("board[",x,"][",y,"] : ", board[x][y])
        return False

def solve():
    global count
    for x in range(n):
        for y in range(n):
            for i in range(8):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if check(x, y):
                        check(nx, ny)
                    else:
                        print("퀸이 중복됨")
                        break
            count+=1
            print(x,",",y,"는 퀸을 놓을 수 있습니다.")
    print(count)

solve()