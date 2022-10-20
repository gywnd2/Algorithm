import sys
n=int(sys.stdin.readline().strip())
coin=list(map(int, sys.stdin.readline().strip().split()))
coin.sort(reverse=True)
check=[False for _ in range(10000001)]
for i in range(1, 1000001):
    tmp=i
    for j in coin:
        if tmp==0:
            continue
        if i-j>=0:
            tmp-=j
    if tmp!=0 and tmp>0:
        print(i)
        break