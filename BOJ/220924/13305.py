import sys

n=int(sys.stdin.readline().strip())
dist=list(map(int, sys.stdin.readline().strip().split()))
oil=list(map(int, sys.stdin.readline().strip().split()))
cost=0
i=0
while i<n-1:
    if oil[i]!=min(oil[:-1]):
        # print("리터 당", oil[i], "원으로", dist[i], "리터 주유합니다.")
        cost+=oil[i]*dist[i]
        # print(dist)
        i+=1
    else:
        # print("리터 당", oil[i], "원(최저가)으로 남은 구간", dist, "모두 주유합니다.")
        cost+=oil[i]*sum(dist[i:])
        break

print(cost)