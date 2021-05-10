import sys
n=int(sys.stdin.readline())
confList=list(list(map(int, sys.stdin.readline().strip().split())) for _ in range(n))
result=[]; idx=0
confList=sorted(confList, key=lambda x:(x[1],x[0]))
result.append(confList[0])
for i in range(1, len(confList)):
    if confList[i][0]>=result[idx][1]:
        result.append(confList[i])
        idx+=1
print(len(result))