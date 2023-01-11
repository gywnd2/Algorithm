import sys
from itertools import combinations
N,M=map(int, sys.stdin.readline().strip().split())
city=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

chicken=[]
house=[]
res=[]

for r in range(N):
    for c in range(N):
        if city[r][c]==1:
            house.append((r,c))
        elif city[r][c]==2:
            chicken.append((r,c))
            
for ch in combinations(chicken, M):
    totalCost=0
    for h in house:
        x, y=h
        minCost=sys.maxsize
        for chicken in ch:
            r, c=chicken
            minCost=min(minCost, abs(x-r)+abs(y-c))
        totalCost+=minCost
    res.append(totalCost)
print(min(res))
            


# def cal(cr, cc):
#     cost=[]
#     for r in range(N):
#         for c in range(N):
#             if city[r][c]==1:
#                 if (r,c) not in house:
#                     house.append((r,c))
#                 cost.append(abs(cr-r)+abs(cc-c))
#     chickenCost.append((sum(cost), cr, cc))

# for r in range(N):
#     for c in range(N):
#         if city[r][c]==2:
#             chicken.append((r,c))
#             cal(r, c)
            
# chickenCost.sort(key=lambda x:x[0])
# chickenCost=chickenCost[:M]

# res=0
# for h in house:
#     nearest=sys.maxsize
#     x, y=h
#     for ch in chickenCost:
#         r, c=ch[1:]
#         nearest=min(nearest, abs(x-r)+abs(y-c))
#     res+=nearest      
# print(res)