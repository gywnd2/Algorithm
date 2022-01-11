import sys
n=int(sys.stdin.readline().strip())
orders=list(map(int, sys.stdin.readline().strip().split()))
series=[0 for _ in range(2000001)]
x=int(sys.stdin.readline().strip())
sol=0

for order in orders:
    series[order]+=1
    
for i in range(n):
    # print("order : ", orders[i])
    if series[orders[i]]==1 and x-orders[i]>0:
        series[orders[i]]=0
        if series[x-orders[i]]==1:
            sol+=1
            # print("orders[i] : ", orders[i], end=' / ')
            # print("x-orders[i] : ", x-orders[i])
            series[x-orders[i]]=0
print(sol)