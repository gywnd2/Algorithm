from collections import deque

n, m=map(int, input().split())
found=0; index=0; count=0; targetIdx=0
target=list(map(int, input().split()))
queue=deque(i for i in range(1, n+1))

# 큐의 중간 지점을 기준으로 좌측에 가까운지 우측에 가까운지 판단
while found!=m:
    targetIdx=queue.index(target[index])
    if queue[0]==target[index]:
        found+=1
        index+=1
        queue.popleft()
    elif targetIdx<=len(queue)//2:
        targetIdx=queue.index(target[index])
        while(queue[0]!=target[index]):
            count+=1
            queue.append(queue.popleft())
    else:
        targetIdx=queue.index(target[index])
        while(queue[0]!=target[index]):
            count+=1
            queue.appendleft(queue.pop())
            
print(count)