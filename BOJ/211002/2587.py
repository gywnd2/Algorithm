num=[]
for _ in range(5):
    num.append(int(input()))
num.sort()
print(sum(num)//len(num))
print(num[2])