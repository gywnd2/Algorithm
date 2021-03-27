num=int(input())
vote=input()
res={"A":0, "B":0}
for i in vote:
    if i=="A":
        res[i]+=1
    else:
        res[i]+=1
if len(list(set(res.values())))==1:
    print("Tie")
else:
    print(max(res, key=res.get))