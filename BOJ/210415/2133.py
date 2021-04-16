import sys
solution=[-1 for _ in range(1001)]
def dp(x):
    solution[0]=1; solution[1]=0; solution[2]=3
    if solution[x]!=-1:
        return solution[x]
    result=3*dp(x-2)
    for i in range(3 , x+1):
        if i%2==0:
            result+=2*dp(x-i)
    return result
print(dp(int(sys.stdin.readline())))