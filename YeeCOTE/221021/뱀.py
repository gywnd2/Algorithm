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
    x, y=1, 1
    while True:
        # time+=1
        # 이동
        nx=x+dx[direction%4]
        ny=y+dy[direction%4]
        
        if orderIdx<l and int(order[orderIdx][0])==time:
            if order[orderIdx][1]=='L':
                if direction>0:
                    direction-=1
                else:
                    direction=3
            else:
                direction=(direction+1)%4
            orderIdx+=1
        
        if 0<nx<=n and 0<ny<=n and (nx, ny) not in snake:
            x, y=nx, ny
            snake.append((x, y))
            if [x, y] in apple:
                # print('사과 발견')
                apple.remove([x, y])
            else:
                snake.popleft()
            
            time+=1
            # print('time :',time, 'direction :', direction, 'snake :', snake, 'nx', nx, 'ny', ny)
        else:
            return
        

bfs()
print(time)
