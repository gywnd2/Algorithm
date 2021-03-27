palin=input()
mid=len(palin)//2
if len(palin)%2!=0:
    if palin[:mid+1]==(palin[mid:])[::-1]:
        print(1)
    else:
        print(0)
elif len(palin)%2==0:
    if palin[:mid]==(palin[mid:])[::-1]:
        print(1)
    else:
        print(0)