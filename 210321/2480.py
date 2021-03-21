num=list(map(int, input().split()))
if len(list(set(num)))==1:
    print(10000+num[0]*1000)
elif len(list(set(num)))==2:
    val=0
    if num.count(num[0])==2:
        val=num[0]
    elif num.count(num[1])==2:
        val=num[1]
    print(1000+val*100)
else:
    num.sort(reverse=True)
    print(num[0]*100)