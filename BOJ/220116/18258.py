from collections import deque
import sys

n=int(sys.stdin.readline().strip())
result=deque()
for _ in range(n):
    command=sys.stdin.readline().strip().split()
    if command[0]=="push":
        result.append(command[1])
    elif command[0]=="pop":
        if len(result)!=0:
            print(result.popleft())
        else:
            print(-1)
    elif command[0]=="size":
        print(len(result))
    elif command[0]=="empty":
        if len(result)==0:
            print(1)
        else:
            print(0)
    elif command[0]=="front":
        if len(result)!=0:
            print(result[0])
        else:
            print(-1)
    else:
        if len(result)!=0:
            print(result[-1])
        else:
            print(-1)