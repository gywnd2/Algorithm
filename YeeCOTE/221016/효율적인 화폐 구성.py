import sys
n, m=map(int, sys.stdin.readline().strip().split())
money=list(int(sys.stdin.readline().strip()) for _ in range(n))
dp=[sys.maxsize for _ in range(m+1)]
dp[0]=0
for i in range(min(money), m+1):
    for j in money:
        if dp[i-j]!=sys.maxsize:
            dp[i]=min(dp[i], dp[i-j]+1)

if dp[m]==sys.maxsize:
    print(-1)
else:
    print(dp[m])