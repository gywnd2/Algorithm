n=int(input())
playerList=[]
for _ in range(n):
    num=int(input())
    playerList=list(list(input().split()) for _ in range(num))
    playerDict={playerList[i][1]:playerList[i][0] for i in range(num)}
    print(max(playerDict, key=playerDict.get))