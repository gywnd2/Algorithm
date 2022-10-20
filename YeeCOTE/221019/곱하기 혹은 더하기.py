import sys
num=list(sys.stdin.readline().strip())
res=0
for i in num:
    if i=='0':
        res+=int(i)
    else:
        if res==0:
            res+=int(i)
        else:
            res*=int(i)
print(res)