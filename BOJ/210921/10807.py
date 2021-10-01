n=int(input())
num=list(map(int, input().split()))
numCount={}
for i in num:
    if i not in numCount:
        numCount[i]=1
    else:
        numCount[i]+=1
v=int(input())
if v in numCount:
    print(numCount[v])
else:
    print(0)