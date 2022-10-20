import sys
n, m=map(int, sys.stdin.readline().strip().split())
balls=list(map(int, sys.stdin.readline().strip().split()))
balls.sort(reverse=True)
count=0
for a in range(n):
    for b in range(a, n):
        if balls[a]!=balls[b]:
            count+=1

print(count)