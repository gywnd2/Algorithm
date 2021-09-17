n=int(input())
count=0
inputList=list(map(int, input().split()))
for num in inputList:
    if num!=1:
        for i in range(2, num):
            if num!=i and num%i==0:
                break
            elif num==i:
                count+=1
            elif i==num-1 and num%i!=0:
                count+=1
print(count)