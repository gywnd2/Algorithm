string=list(input())
res=[]
for chr in string:
    if chr.isupper():
        res.append(chr.lower())
    else:
        res.append(chr.upper())
print("".join(res))