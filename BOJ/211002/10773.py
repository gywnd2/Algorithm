k=int(input())
num=[]
recentNum=[]
for _ in range(k):
    num.append(int(input()))
for i in range(len(num)):
    if num[i]!=0:
        recentNum.append(num[i])
    else:
        recentNum.pop()
print(sum(recentNum))