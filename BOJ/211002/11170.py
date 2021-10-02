t=int(input())
for _ in range(t):
    res=0
    a, b=map(int, input().split())
    for num in range(a, b+1):
        num=list(str(num))
        for digit in num:
            if digit=="0":
                res+=1
    print(res)