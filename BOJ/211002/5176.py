k=int(input())
for _ in range(k):
    seat=[0]*501
    res=0
    p, m=map(int, input().split())
    for _ in range(p):
        n=int(input())
        if seat[n]!=1:
            seat[n]=1
        else:
            res+=1
    print(res)