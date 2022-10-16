import sys
sys.setrecursionlimit(100000)
x=int(sys.stdin.readline().strip())
dp=[0 for _ in range(x+1)]
dp[x]=0
# def solution(i):
#     if i==1:
#         return
#     dp[i-1]=min(dp[i-1], dp[i]+1)
#     solution(i-1)
#     if i%5==0:
#         dp[i//5]=min(dp[i//5], dp[i]+1)
#         solution(i//5)
#     if i%3==0:
#         dp[i//3]=min(dp[i//3], dp[i]+1)
#         solution(i//3)
#     if i%2==0:
#         dp[i//2]=min(dp[i//2], dp[i]+1)
#         solution(i//2)

for i in range(2, x+1):
    dp[i]=dp[i-1]+1
    if i%2==0:
        dp[i]=min(dp[i], dp[i//2]+1)
    if i%3==0:
        dp[i]=min(dp[i], dp[i//3]+1)
    if i%5==0:
        dp[i]=min(dp[i], dp[i//5]+1)
        
print(dp[x])