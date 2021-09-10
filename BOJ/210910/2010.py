n=int(input())
result=1
plugs=[int(input()) for _ in range(n)]
for com in plugs:
    if com>1:
        result+=(com-1)
print(result)