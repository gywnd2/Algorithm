n=int(input())
prize=[]
for _ in range(n):
    num={}
    dice=list(map(int, input().split()))
    for i in dice:
        try:
            num[i]+=1
        except:
            num[i]=1
    dice=list(set(dice))
    numVal=list(num.values())
    numKey=list(num.keys())
    dupl=numKey[numVal.index(max(num.values()))]
    if len(dice)==1:
        prize.append(10000+dice[0]*1000)
    elif len(dice)==2:
        prize.append(1000+dupl*100)
    else:
        prize.append(max(dice)*100)
print(max(prize))