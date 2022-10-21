import sys
from collections import deque
n=int(sys.stdin.readline().strip())
k=int(sys.stdin.readline().strip())
apple=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(k)]
l=int(sys.stdin.readline().strip())
order=[list(sys.stdin.readline().strip().split()) for _ in range(l)]

dx, dy=[0, 1, 0, -1], [1, 0, -1, 0]
time=0
snake=deque([(1, 1)])

def bfs():
    global time
    orderIdx=0
    direction=0
    # print(apple)
    while True:
        # 뱀 이동
        if orderIdx<len(order):
            orderTime, orderDirection=int(order[orderIdx][0]), order[orderIdx][1]                
            x, y=snake[-1][0], snake[-1][1]   

        # 이동
        nx=x+dx[direction%4]
        ny=y+dy[direction%4]
        
        print('time :',time, 'direction :', direction, 'snake :', snake, 'nx', nx, 'ny', ny)
        # 방향전환
        if orderTime==time:
            if orderDirection=='L':
                if direction>0:
                    direction-=1
                else:
                    direction=3
            elif orderDirection=='D':
                direction=(direction+1)%4
            orderIdx+=1 
        
        
        if nx<1 or nx>n or ny<1 or ny>n or (nx, ny) in snake:
            # print(True if (nx, ny) in snake else False)
            # print('몸통 발견')
            return
        elif 0<nx<=n and 0<ny<=n:
            x, y=nx, ny
            snake.append((nx, ny))
            if [nx, ny] in apple:
                # print('사과 발견')
                apple.remove([nx, ny])
            else:
                snake.popleft()
            time+=1
        

bfs()
print(time)
