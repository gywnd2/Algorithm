import sys
string=list(sys.stdin.readline().strip())
res=[]; num=0
for i in string:
    if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        num+=int(i)
    else:
        res.append(i)
res.sort()
res.append(str(num))
print(''.join(res))