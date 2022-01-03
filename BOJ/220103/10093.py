a, b=map(int, input().split())
if a==b:
    print(0)
else:
    print(max(a, b)-min(a, b)-1)
    for i in range(min(a, b)+1, max(a, b)):
        print(i, end=' ')