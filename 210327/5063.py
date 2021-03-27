n=int(input())
for _ in range(n):
    val=list(map(int, input().split()))
    est=val[0]-(val[1]-val[2])
    if est<0:
        print("advertise")
    elif est>0:
        print("do not advertise")
    else:
        print("does not matter")