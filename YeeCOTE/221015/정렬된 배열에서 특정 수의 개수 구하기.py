import sys
n, x=map(int, sys.stdin.readline().strip().split())
num=list(map(int, sys.stdin.readline().strip().split()))

start=bisect_left(num, x)+1
end=bisect_left(num, x)+1

if len(num[start:end])==0:
    print(-1)
else:
    print(len(num[start:end]))