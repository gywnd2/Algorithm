def selfNum():
    num=1
    sum=0
    genList = list()
    numList = list(i + 1 for i in range(9999))
    print(numList)
    while sum<=10000:
        sum=0
        sum += num
        num=str(num)

        for n in num:
            sum += int(n)
        genList.append(sum)
        num=int(num)+1

    for i in genList:
        if i in numList:
            numList.remove(i)

    for n in numList:
       print(n)


selfNum()

