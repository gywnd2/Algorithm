n=int(input())
pan=[[0]*19 for _ in range(19)] #단순 곱으로 초기화 하면 같은 리스트를 참조하는 레퍼런스로 인식하여 다같이 값이 바뀐다
for i in range(n):
    x, y=map(int, input().split())
    pan[x-1][y-1]=1
for i in pan:
    for j in i:
        print(j, end=' ')
    print()