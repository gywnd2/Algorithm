def fiboRecur(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fiboRecur(num-1)+fiboRecur(num-2)

def fiboIter(num):
    fib=[0 for _ in range(num+1)]
    fib[0]=0; fib[1]=1
    for i in range(2, num+1):
        fib[i]=fib[i-1]+fib[i-2]
    print(fib)
    return fib[num]

num=int(input())
solution=[-1 for _ in range(num+1)]
def fiboDP(num):
    solution[0]=0; solution[1]=1
    if solution[num]!=-1:
        return solution[num]
    for i in range(2, num+1):
        solution[i]=solution[i-1]+solution[i-2]
    return solution[num]
print(fiboDP(num))