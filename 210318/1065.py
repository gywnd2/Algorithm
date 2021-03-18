upperBound=input()
num=list(i for i in range(1, int(upperBound)+1))
hs=0
for number in num:
    if number<100:
        hs+=1
    else:
        number = str(number)
        if int(number[1])-int(number[0])==int(number[2])-int(number[1]):
            hs+=1

print(hs)