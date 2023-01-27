import sys
input=sys.stdin.readline
K, P, N=map(int, input().strip().split())
result=K

def solution(x, y):
    if y==1:
        return x
    elif y%2==0:
        return solution(x, y//2)*solution(x, y//2)%1000000007
    else:
        return x*solution(x, (y-1)//2)*solution(x, (y-1)//2)%1000000007

result=solution(P, 10*N)
result*=K
print(result)