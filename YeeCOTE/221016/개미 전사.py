import sys
n=int(sys.stdin.readline().strip())
storage=list(map(int, sys.stdin.readline().strip().split()))
dp=[0 for _ in range(100)]
dp[0], dp[1]=storage[0], storage[1]

for i in range(2,  n):
    dp[i]=max(dp[i-1], dp[i-2]+storage[i])

print(dp[n-1])