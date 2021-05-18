map=[[97+i for i in range(8)] for _ in range(8)]
currLoc=input()
order={(-2, 1),(-2,-1),(2,1),(2,-1),(1,2),(-1,2),(1,-2),(-1,-2)}
locX=0; locY=int(currLoc[1])-1; count=0
if ord(currLoc[0]) in map[0]:
    locX=map[0].index(ord(currLoc[0]))
for proc in order:
    if not(0<=locX+proc[0]<=7):
        pass
    elif (0<=locX+proc[0]<=7) and (0<=locY+proc[1]<=7):
        count+=1
print(count)