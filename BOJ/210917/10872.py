n=int(input())
facList=[-1]*13
facList[0]=1; facList[1]=1
def factorial(n):
    if facList[n]==-1:
        return n*factorial(n-1)
    else:
        return facList[n]
print(factorial(n))