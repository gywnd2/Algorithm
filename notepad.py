import sys

N = int(sys.stdin.readline())
assembly_line = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

# Dynamic Programiing 활용
dp = [[0,0]] * N
dp[0] = [assembly_line[0][0], assembly_line[0][1]]

for i in range(1, N):
    dp[i] = [min(dp[i-1][0], dp[i-1][1] + assembly_line[i-1][3]) + assembly_line[i][0], # A 조립라인
             min(dp[i-1][1], dp[i-1][0] + assembly_line[i-1][2]) + assembly_line[i][1]] # B 조립라인

print(min(dp[N-1])) 


# import sys
# n=int(sys.stdin.readline().strip())
# #Ai / Bi / Ai to Bi+1 / Bi to Ai+1 / AN / BN
# cost=list(map(int, sys.stdin.readline().strip().split()))
# cost.extend(list(map(int, sys.stdin.readline().strip().split())))
# dp=[[0 for _ in range(n)] for _ in range(2)]
# dp[0][0], dp[1][0]=cost[0], cost[1]
# for i in range(1, n):
#     if i<n-1:
#         dp[0][i]=min(dp[0][i-1], dp[1][i-1]+cost[3])+cost[0]
#         dp[1][i]=min(dp[1][i-1], dp[0][i-1]+cost[2])+cost[1]
#     else:
#         dp[0][i]=min(dp[0][i-1], dp[1][i-1]+cost[3])+cost[4]
#         dp[1][i]=min(dp[1][i-1], dp[0][i-1]+cost[2])+cost[5]
# print(min(dp[0][n-1], dp[1][n-1]))