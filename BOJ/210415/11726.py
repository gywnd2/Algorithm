import sys
n=int(sys.stdin.readline())
solution=[0 for _ in range(1001)]
def dp(x):
    solution[1]=1; solution[2]=2
    for i in range(3, len(solution)):
        solution[i]=solution[i-1]+solution[i-2]
    return solution[x]
print(dp(n)%10007)