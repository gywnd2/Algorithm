n=list(input())
res=0
for i in range(len(n)):
    if int(n[i])<2 or res<2:
        res+=int(n[i])
    else:
        res*=int(n[i])
print(res)