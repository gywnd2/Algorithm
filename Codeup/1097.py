a=[]
b=[]
c=[]
for _ in range(19):
    b=list(map(int, input().split()))
    a.append(b)

n=int(input())

for _ in range(n):
    x, y=map(int, input().split())
    c.append([x,y])
#for m in range(n)이 있을 경우 n=2이 입력되어 원래상태로 복구됨 애초에 필요가 없는 문장
for i in c:
    r=i[0]-1
    for j in range(19):
        if a[r][j]==0:
            a[r][j]=1
        else:
            a[r][j]=0

for k in c:
    w=k[1]-1
    for j in range(19):
        if a[j][w]==0:
            a[j][w]=1
        else:
            a[j][w]=0

for happy in a:
    for omg in happy:
        print(omg, end=' ')
    print()