t=int(input())
dist=[]
for _ in range(t):
    res=[]
    x, y=map(str, input().split())
    x=list(x)
    y=list(y)
    for i in range(len(x)):
        if ord(x[i])<=ord(y[i]):
            res.append(ord(y[i])-ord(x[i]))
        elif ord(x[i])>ord(y[i]):
            res.append(ord(y[i])+26-ord(x[i]))
    dist.append(res)

for case in dist:
    print("Distances: ", end='')
    for i in case:
        print(i, end=' ')
    print()