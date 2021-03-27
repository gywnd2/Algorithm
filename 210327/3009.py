squarePos=[]
xPos=[]
yPos=[]
x={}
y={}
for _ in range(3):
    pos=list(map(int, input().split()))
    xPos.append(pos[0])
    yPos.append(pos[1])
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
reqX=min(x.values())
reqY=min(y.values())
xKey=list(x.keys())
yKey=list(y.keys())
xVal=list(x.values())
yVal=list(y.values())
reqX=xKey[xVal.index(reqX)]
reqY=yKey[yVal.index(reqY)]
print(reqX, reqY)