import sys
n=int(sys.stdin.readline().strip())
soldiers=list(map(int, sys.stdin.readline().strip().split()))
dp=[1 for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if soldiers[j]>soldiers[i]:
            dp[i]=max(dp[i], dp[j]+1)

print(n-max(dp))