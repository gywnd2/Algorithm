caseNum=int(input())
inputList=list()
for _ in range(caseNum):
    inputLine=list()
    repeatNum, originStr = input().split()
    inputLine.append(repeatNum)
    inputLine.append(originStr)
    inputList.append(inputLine)

for line in inputList:
    for str in line[1]:
        for _ in range(int(line[0])):
            print(str, end='')
    print()