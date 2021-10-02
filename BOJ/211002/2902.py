memo=list(input())
res=[]
res.append(memo[0])
for i in range(len(memo)):
    if ord(memo[i])==45:
        res.append(memo[i+1])
print(''.join(res))