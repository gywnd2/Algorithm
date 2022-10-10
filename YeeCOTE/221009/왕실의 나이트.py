import sys
pos=list(sys.stdin.readline().strip())
mov=[[2,-1],[-2,1],[2,1],[-2,-1],[1,-2],[-1,-2],[-1,2],[1,2]]
count=0

for m in mov:
    nx=ord(pos[0])-96+m[0]
    ny=int(pos[1])+m[1]
    if 1<=nx<=8 and 1<=ny<=8:
        count+=1

print(count)