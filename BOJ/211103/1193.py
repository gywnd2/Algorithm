import sys
x=int(sys.stdin.readline())
pyramid=[]
rowSize=1
length=0
while rowSize<x:
    x-=rowSize
    rowSize+=1
if(rowSize%2==0):
    print(str(x)+"/"+str(rowSize-(x-1)))
else:
    print(str(rowSize-(x-1))+"/"+str(x))