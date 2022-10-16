import sys
t=int(sys.stdin.readline().strip())
for _ in range(t):
    n, m=map(int, sys.stdin.readline().strip().split())
    dp=[[0 for _ in range(m)] for _ in range(n)]
    gold=list(map(int, sys.stdin.readline().strip().split()))
    gold=list(gold[i:i+m] for i in range(0, n*m, m))
    for i in range(n):
        dp[i][0]=gold[i][0]
        
    for j in range(1, m):
        for i in range(n):
            if 0<i<n-1:
                dp[i][j]=gold[i][j]+max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])
            if i==n-1:
                dp[i][j]=gold[i][j]+max(dp[i-1][j-1], dp[i][j-1])
            if i==0:
                dp[i][j]=gold[i][j]+max(dp[i][j-1], dp[i+1][j-1])
    res=dp[0][m-1]
    for i in range(n):
        if dp[i][m-1]>res:
            res=dp[i][m-1]
            
    print(res)