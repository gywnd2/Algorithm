t=int(input())
for _ in range(t):
    num=list(map(int, input().split()))
    num.sort()
    print(num[-3])