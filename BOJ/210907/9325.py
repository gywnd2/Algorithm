n=int(input())
for _ in range(n):
    s=int(input())
    m=int(input())
    for _ in range(m):
        q, p=map(int, input().split())
        s+=q*p
    print(s)