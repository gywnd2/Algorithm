list=[]
while True:
    num=int(input())
    if num==-1:
        break
    div=[]
    for d in range(1, num):
        if num%d==0:
            div.append(d)
    if sum(div)==num:
        print("%d = %d" %(num, div[0]), end='')
        for i in range(1, len(div)):
            print(" + %d" %div[i],end='')
        print()
    else:
        print("%d is NOT perfect."%num)