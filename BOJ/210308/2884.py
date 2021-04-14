h, m=map(int, input().split())

if h>0 and m<45:
    print("%d %d" % (h-1, 60-(45-m)))
elif h==0 and m<45:
    print("%d %d" % (23, 60-(45-m)))
else:
    print("%d %d" % (h, m-45))