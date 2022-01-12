import sys
# import time
# Doubly linked list로 구현 됨
# deque 짱짱!
from collections import deque

lStack=sys.stdin.readline().strip()
n=int(sys.stdin.readline())
# start=time.time()

lStack=deque(lStack)
# 스택
rStack=deque()

# 명령 입력
commands=[]
for _ in range(n):
    commands.append(sys.stdin.readline().strip())
    
for command in commands:
    if command[0]=="P":
        # O(1)
        lStack.append(command[2])
    elif command[0]=="L":
        if len(lStack)!=0:
            # O(1)
            rStack.appendleft(lStack.pop())
    elif command[0]=="D":
        if len(rStack)!=0:
            # O(1)
            lStack.append(rStack[0])
            # O(1)
            rStack.popleft()
    # B
    else:
        if len(lStack)!=0:
            # O(1)
            lStack.pop()
# end=time.time()
print("".join(lStack+rStack))
# print(end-start)