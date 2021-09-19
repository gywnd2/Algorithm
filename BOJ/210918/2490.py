for _ in range(3):
    yut=map(int, input().split())
    result=sum(yut)
    if result==3:
        print("A")
    elif result==2:
        print("B")
    elif result==1:
        print("C")
    elif result==0:
        print("D")
    else:
        print("E")