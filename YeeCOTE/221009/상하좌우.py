import sys
n=int(sys.stdin.readline().strip())
cmd=list(map(str, sys.stdin.readline().strip().split()))
curPos=[1, 1]
for i in cmd:
    if i=='L':
        if 2<=curPos[1]:
            curPos[1]-=1
    elif i=='R':
        if curPos[1]<5:
            curPos[1]+=1
    elif i=='U':
        if 2<=curPos[0]:
            curPos[0]-=1
    elif i=='D':
        if curPos[0]<5:
            curPos[0]+=1

print(curPos[0], curPos[1])