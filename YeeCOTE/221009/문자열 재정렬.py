import sys
s=list(sys.stdin.readline().strip())
res=[]
tmp=[]
for char in s:
    if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        res.append(char)
    else:
        tmp.append(int(char))
res.sort()
res.append(str(sum(tmp)))
print(''.join(res))