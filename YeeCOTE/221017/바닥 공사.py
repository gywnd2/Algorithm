import sys
n=int(sys.stdin.readline().strip())
dp=[0 for _ in range(n)]
dp[0], dp[1]=1, 3
for i in range(2, n):
    dp[i]=dp[i-1]+dp[i-2]*2
print(dp[n-1]%796796)