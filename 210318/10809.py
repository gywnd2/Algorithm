word=input()
alphabet=list(-1 for _ in range(26))
for idx in range(len(word)):
    if alphabet[ord(word[idx])-97]!=-1:
        pass
    else:
        alphabet[ord(word[idx]) - 97] += (idx + 1)
for element in alphabet:
    print("%s "%element, end='')