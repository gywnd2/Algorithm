t=int(input())
for _ in range(t):
    inputList=list(input().split())
    inputList[0]=int(inputList[0])
    inputList[1]=list(inputList[1])
    inputList[1].pop(inputList[0]-1)
    print(''.join(inputList[1]))