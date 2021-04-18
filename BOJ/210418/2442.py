import sys
n=int(sys.stdin.readline())
for i in range(1, n+1):
    if i==1:
        a=(2*n-1-1)//2
        print(' '*a, end='')
        print('*'*(2*i-1),end='')
        print()
    elif i==n:
        print('*'*(2*i-1), end='')
    else:
        a=(2*n-1-2*(i-1))//2
        print(' '*a, end='')
        print('*'*(2*i-1), end='')
        print()