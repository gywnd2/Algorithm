import sys
num=list(sys.stdin.readline().strip())
countOne, countZero=0, 0; switch=int(num[0])
if int(num[0])==1:
    countOne+=1
else:
    countZero+=1
    
for i in num:
    if int(i)!=switch:
        if int(i)==1:
            countOne+=1
        else:
            countZero+=1
        switch=int(i)
print(min(countOne, countZero))