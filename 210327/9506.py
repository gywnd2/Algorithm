list=[]
while sum<100000:
    sum=0
    for n in range(1, 100000):
        sum+=n
        list.append(sum)
        print("appending", sum)
while int(input())!=-1:
    num=int(input())
    if num in list:
        print("")