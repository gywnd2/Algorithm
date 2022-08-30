import sys

n, m=map(int, sys.stdin.readline().strip().split())
selected=[0 for _ in range(n+1)]
series=[-1 for _ in range(m)]

def check(k):
    if k==m:
        for num in series:
            if num!=-1:
                print(num, end=' ')
        print()
        return

    for i in range(1, n+1):
        if not selected[i]:
            series[k]=i
            selected[i]=1
            check(k+1)
            selected[i]=0

check(0)