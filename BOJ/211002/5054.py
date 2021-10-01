t=int(input())
shop=[]
for _ in range(t):
    res=0
    n=int(input())
    shop=list(map(int, input().split()))
    shop.sort()
    for i in range(1, len(shop)):
        res+=(shop[i]-shop[i-1])
    print(res*2)