n=int(input())
count=0
inputList=list(map(int, input().split()))
for num in inputList:
    if num!=1:
        if num==2:
            count+=1
        for i in range(2, num):
            if num%i==0:
                break
            elif i==num-1:
                if num%i!=0:
                    count+=1
print(count)