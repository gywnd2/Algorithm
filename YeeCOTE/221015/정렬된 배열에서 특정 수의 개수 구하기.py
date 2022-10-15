import sys
from bisect import bisect_left, bisect_right
n, x=map(int, sys.stdin.readline().strip().split())
num=list(map(int, sys.stdin.readline().strip().split()))

start=bisect_left(num, x)
end=bisect_right(num, x)

if end-start==0:
    print(-1)
else:
    print(end-start)