n=int(input())
aPoint=100; bPoint=100
for _ in range(n):
    a, b=map(int, input().split())
    if a>b:
        bPoint-=a
    elif a<b:
        aPoint-=b
print(aPoint, bPoint)
