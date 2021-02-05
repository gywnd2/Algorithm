a=int(input())
b=0
for n in range(1,a+1):
    b+=n
    if b>=a:
        print(n)
        break