numList=[int(input()) for _ in range(10)]
numDict={}
for num in numList:
    if num not in numDict:
        numDict[num]=1
    else:
        numDict[num]+=1
print(sum(numList)//len(numList))
for key, value in numDict.items():
    if value==max(numDict.values()):
        print(key)