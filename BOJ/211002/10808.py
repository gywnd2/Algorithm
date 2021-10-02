s=list(input())
dic=[0]*26
for ch in s:
    dic[ord(ch)-97]+=1
for i in range(len(dic)):
    print(dic[i], end=' ')