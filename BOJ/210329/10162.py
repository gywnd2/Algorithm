t=int(input())
aCount=0;bCount=0;cCount=0
aCount=t//300
t=t-300*aCount
bCount=t//60
t=t-60*bCount
cCount=t//10
t=t-10*cCount
if t!=0:
    print(-1)
else:
    print(aCount, bCount, cCount)