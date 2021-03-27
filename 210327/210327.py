n=int(input())
quadrant={"Q1" : 0, "Q2" : 0, "Q3" : 0, "Q4" : 0, "AXIS" : 0}
for _ in range(n):
    x, y=map(int, input().split())
    if x>0 and y>0:
        quadrant["Q1"]+=1
    elif x<0 and y>0:
        quadrant["Q2"]+=1
    elif x<0 and y<0:
        quadrant["Q3"]+=1
    elif x>0 and y<0:
        quadrant["Q4"]+=1
    else:
        quadrant["AXIS"]+=1
keyList=list(quadrant.keys())
valList=list(quadrant.values())
for i in range(len(keyList)):
    print("%s: %s"%(keyList[i],valList[i]))