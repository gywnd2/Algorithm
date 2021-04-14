def LCM(a,b):
    d=GCD(a,b)
    return int((a*b)/d)
def GCD(a,b):
    return GCD(b%a, a) if b%a else a

t=int(input())
for _ in range(t):
    a, b=map(int, input().split())
    print(LCM(a,b))