squarePos=[]
for _ in range(3):
    pos=list(map(int, input().split()))
    squarePos.append(pos)
xPos=[squarePos[0][0], squarePos[1][0], squarePos[2][0]]
yPos=[squarePos[0][1], squarePos[1][1], squarePos[2][1]]
x={}
y={}
for i in xPos:
    try:
        x[i]+=1
    except:
        x[i]=1
for i in yPos:
    try:
        y[i]+=1
    except:
        y[i]=1
targetX=0
targetY=0
print(x)
print(y)
xPos=list(set(xPos))
yPos=list(set(yPos))
if x[xPos[0]]<