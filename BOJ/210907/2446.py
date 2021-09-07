n=int(input())
for i in range(2*n-1):
    if (2*n-1-2*i)<1:
        break
    print(" "*(2*i//2),end='')
    print("*"*(2*n-1-2*i), end='')
    print()
for i in range(1, n):
    print(" "*((2*n-1-(2*i+1))//2),end='')
    print("*"*(2*i+1), end='')
    print()