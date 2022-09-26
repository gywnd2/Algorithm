import sys

n=int(sys.stdin.readline().strip())
dist=list(map(int, sys.stdin.readline().strip().split()))
oil=list(map(int, sys.stdin.readline().strip().split()))
minCost=oil[0]
cost=dist[0]*oil[0]
for i in range(1, n-1):
    if minCost>oil[i]:
        minCost=oil[i]
    cost+=minCost*dist[i]
    
print(cost)