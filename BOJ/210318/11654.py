inputNum=list(input() for _ in range(2))
n, digit=map(int, inputNum)
digit=str(digit)
sum=0
for i in digit:
    sum+=int(i)
print(sum)