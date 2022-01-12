count=0
before=input()
after=input()
bChar=[0 for _ in range(26)]; aChar=[0 for _ in range(26)]
for char in before:
    bChar[ord(char)-97]+=1
for char in after:
    aChar[ord(char)-97]+=1
for i in range(26):
    if bChar[i]!=aChar[i]:
        count+=(max(bChar[i], aChar[i])-min(bChar[i], aChar[i]))
# print(bChar)
# print(aChar)
print(count)