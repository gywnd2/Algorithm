r, g, b=map(int, input().split())
count=0
for rn in range(0,r):
    for gn in range(0,g):
        for bn in range(0,b):
            print("%d %d %d" %(rn, gn, bn))
            count+=1
print(count)