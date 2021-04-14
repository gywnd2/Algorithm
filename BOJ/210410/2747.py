import sys
n=int(sys.stdin.readline())
fiboMem=list(0 for _ in range(n+1))
def fibonacci(num):
    if num==1 or num==2:
        fiboMem[num]=1
    elif fiboMem[num]!=0:
        return fiboMem[num]
    else:
        fiboMem[num]=fibonacci(num-1)+fibonacci(num-2)
    return fiboMem[num]
print(fibonacci(n))