import sys
t=int(sys.stdin.readline())
def fibDP(x):
    if x==0 or x==1:
        return fibMem[x]
    for i in range(2, x+1):
        fibMem.append([fibMem[i-1][0]+fibMem[i-2][0],fibMem[i-1][1]+fibMem[i-2][1]])
    return fibMem[x]
for _ in range(t):
    fibMem = [[1,0],[0,1]]
    res=fibDP(int(sys.stdin.readline()))
    print(res[0], res[1])