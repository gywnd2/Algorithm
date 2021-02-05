n=int(input())
student=list(map(int, input().split()))
for j in reversed(student):
    print("%d " %j,end='')