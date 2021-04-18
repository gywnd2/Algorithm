import sys
n=int(sys.stdin.readline())
remain=0
for i in range(n):
    a, b=sys.stdin.readline().split()
    a=int(a); b=int(b)
    remain+=(b-(a*(b//a)))
print(remain)