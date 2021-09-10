n=int(input())
for _ in range(n):
    c, v=map(int, input().split())
    quotient=c//v
    remainder=c%v
    print("You get ", end='')
    print(quotient,end='')
    print(" piece(s) and your dad gets ",end='')
    print(remainder, end='')
    print(" piece(s).")