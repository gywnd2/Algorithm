import sys
n=int(sys.stdin.readline())
p=list(map(int, sys.stdin.readline().strip().split()))
p.sort(); res=0
for i in range(1,n+1):
    temp=p[:i]
    res+=sum(temp)
print(res)