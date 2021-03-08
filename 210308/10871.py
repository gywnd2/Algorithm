n, x=map(int, input().split())
l=input().split()
l=list(map(int, l))

for i in range(n):
    if l[i]<x:
        print("%d " % l[i], end='')
        continue