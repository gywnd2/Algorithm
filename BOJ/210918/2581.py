m=int(input())
n=int(input())
prime=[]
for i in range(m, n+1):
    if i>1:
        if i==2:
            prime.append(i)
        for num in range(2, i):
            if i%num==0:
                break
            elif num==i-1:
                if num%i!=0:
                    prime.append(i)
if len(prime)==0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))