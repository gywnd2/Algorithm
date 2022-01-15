from collections import deque
import sys

t=int(sys.stdin.readline().strip())
for _ in range(t):
    l=list(sys.stdin.readline().strip())
    command=[]
    lStack=deque()
    rStack=deque()
        
    for order in l:
        if order=="<":
            if len(lStack)!=0:
                rStack.appendleft(lStack.pop())
        elif order==">":
            if len(rStack)!=0:
                lStack.append(rStack.popleft())
        elif order=="-":
            if len(lStack)!=0:
                lStack.pop()
        else:
            lStack.append(order)
    
    print("".join(lStack+rStack))