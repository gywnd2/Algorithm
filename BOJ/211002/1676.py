n=int(input())
res=0
def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)
num=list(str(factorial(n)))
num=num[::-1]
for digit in num:
    if digit=="0":
        res+=1
    else:
        print(res)
        break