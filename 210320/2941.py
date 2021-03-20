word=input()
count=0
croatian=["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for j in croatian:
    if j in word:
        word=word.replace(j, "!")
print(len(word))