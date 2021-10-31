n=int(input())
result=1; count=1; current=1
while current<n:
    result+=count
    current+=6*count
    count+=1
print(count)