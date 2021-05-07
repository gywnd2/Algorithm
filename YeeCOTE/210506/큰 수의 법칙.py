N,M,K=map(int, input().split())
num=list(map(int, input().split()))
num.sort(reverse=True)
res=[]
while True:
    for i in range(K):
        if len(res)>=M:
           break
        res.append(num[0])
    if len(res)>=M:
        break    
    res.append(num[1])
print(sum(res))