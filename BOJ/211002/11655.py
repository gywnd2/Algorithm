string=list(input())
alphabet='abcdefghijklmnopqrstuvwxyz'
res=[]
for ch in string:
    if ch.islower():
        idx=(alphabet.index(ch)+13)%26
        res.append(alphabet[idx])
    elif ch.isupper():
        ch=ch.lower()
        idx=(alphabet.index(ch)+13)%26
        res.append(alphabet[idx].upper())
    else:
        res.append(ch)
print(''.join(res))