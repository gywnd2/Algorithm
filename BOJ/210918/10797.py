date=int(input())
car=list(map(int, input().split()))
count=0
for number in car:
    if date==number:
       count+=1
print(count)