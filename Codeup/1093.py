n=int(input())
student=list(map(int, input().split()))
a=[0]*23
for i in student:
    a[i-1]+=1
for j in range(0, len(a)):
    print(a[j],end='')
    if j!=len(a):
        print(" ",end='')