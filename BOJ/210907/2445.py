n=int(input())
for i in range(0, n):
    print("*"*(i+1), end='')
    print(" "*2*(n-(i+1)), end='')
    print("*"*(i+1),end='')
    print()
    # if i==n-1:
    #     print("*"*(2*n))
for i in range(n-1, 0,-1):
    print("*"*i, end='')
    print(" "*2*(n-i), end='')
    print("*"*i,end='')
    print()