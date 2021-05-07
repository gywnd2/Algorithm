import sys
a, b, c=map(int, sys.stdin.readline().strip().split())
if b==c:
    print(-1)
elif -a//(b-c)+1>0:
    print(-a//(b-c)+1)
else:
    print(-1)