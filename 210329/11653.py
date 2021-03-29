n=int(input())
res=[]
def prime_list(n):
    sieve=[True]*n
    m=int(n**0.5)
    for i in range(2, m+1):
        if sieve[i]==True:
            for j in range(i+i, n, i):
                sieve[j]=False
    return [i for i in range(2,n) if sieve[i]==True]
prime=prime_list(10000000)
for pr in prime:
    if pr>n:
        break
    pow = 1
    while True:
        if n % (pr ** pow) != 0:
            break
        elif n%(pr**pow)==0:
            pow += 1
    n=n//(pr**(pow-1))
    for _ in range(1, pow):
        res.append(pr)
for i in res:
    print(i)