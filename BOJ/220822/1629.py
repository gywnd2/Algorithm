import sys
sys.setrecursionlimit(100000)

a, b, c=map(int, sys.stdin.readline().strip().split())

def solve(a, b, c):
    if b==1:
        return a%c
    val=solve(a, b//2, c)
    if b%2==0:
        return val*val%c
    return val*val*a%c

print(solve(a, b, c))