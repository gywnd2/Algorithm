import sys
n, k=map(int, sys.stdin.readline().strip().split())
a=list(map(int, sys.stdin.readline().strip().split()))
b=list(map(int, sys.stdin.readline().strip().split()))

a.sort()
b.sort()
idx=1; i=0
while i<k:
    if a[i]<b[-idx]:
        a[i], b[-idx]=b[-idx], a[i]
        i+=1
    idx+=1
print(sum(a))