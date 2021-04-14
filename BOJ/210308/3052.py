num=list(int(input()) for _ in range(10))
rem=list()
for i in range(len(num)):
    find=num[i]%42
    rem.append(find)

rem=set(rem)
rem=list(rem)
print(len(rem))