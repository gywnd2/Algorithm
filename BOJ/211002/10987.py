vowel=['a', 'e', 'i', 'o', 'u']
count=0
string=list(input())
for ch in string:
    if ch in vowel:
        count+=1
print(count)