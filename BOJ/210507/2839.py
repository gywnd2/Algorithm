n=int(input())
count=0
while True:
    while n>=3:
        if n%5==0:
            count+=(n//5)
            n%=5
        else:
            count+=1
            n-=3
    if n==0:
        print(count)
        break
    else:
        print(-1)
        break