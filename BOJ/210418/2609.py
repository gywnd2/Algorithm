import sys
a, b=map(int, sys.stdin.readline().split())
def GCD(a, b):
    cd=[]
    for i in range(1, max(a,b)+1):
        if a%i==0 and b%i==0:
            cd.append(i)
    return max(cd)    
def LCM(a, b):
    return int(a*b/GCD(a, b))
print(GCD(a,b))
print(LCM(a,b))