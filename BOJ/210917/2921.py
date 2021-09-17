n=int(input())
count=0
for i in range(n+1):
    count+=i
    for j in range(n+1):
        count+=j
print(count)