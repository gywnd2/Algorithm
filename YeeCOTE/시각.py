N=int(input())
count=0
for i in range((N+1)*3600):
    h=i//3600
    m=(i%3600)//60
    s=(i%3600)%60
    if h%10==3:
        count+=1
    elif m%10==3 or m//10==3:
        count+=1
    elif s%10==3 or s//10==3:
        count+=1
print(count)