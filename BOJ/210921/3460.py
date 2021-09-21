t=int(input())
result=[]
for _ in range(t):
    num=bin(int(input()))
    num=list(str(num))
    num=num[2:]
    num.reverse()
    for i in range(len(num)):
        if num[i]=='1':
            result.append(i)
for pos in result:
    print(pos, end=' ')