N=int(input())
for i in range(N, 0, -1):
    star=2*N-(2*i-1); blank=(2*N-star)//2
    print(" "*blank,end='')
    print("*"*star,end='')
    print()
for i in range(2, N+1):
    star=2*N-(2*i-1); blank=(2*N-star)//2
    print(" "*blank,end='')
    print("*"*star,end='')
    if star!=1:
        print()