n=int(input())
subscore=input().split()
subscore=list(map(int, subscore))

global max, sum
max=subscore[0]
sum=0

for i in range(n):
    if max<subscore[i]:
        max=subscore[i]

for i in range(n):
    subscore[i]=subscore[i]/max*100
    sum+=subscore[i]

print(sum/n)