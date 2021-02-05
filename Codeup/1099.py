maze=[list(map(int, input().split())) for _ in range(10)]
xPos=1
yPos=1
while True:
    if maze[xPos][yPos]==0:
        maze[xPos][yPos]=9
        yPos+=1
    elif maze[xPos][yPos]==1:
        if maze[xPos+1][yPos-1]==1:
            break
        yPos-=1
        xPos+=1
    elif maze[xPos][yPos]==2:
        maze[xPos][yPos]=9
        break

for i in maze:
    for j in i:
        print(j, end=' ')
    print()