n=int(input())
for _ in range(n):
    before, after=input().split()
    bChar=[0 for _ in range(26)]; aChar=[0 for _ in range(26)]
    for char in before:
        bChar[ord(char)-97]+=1
    for char in after:
        aChar[ord(char)-97]+=1
    if bChar==aChar:
        print("Possible")
    else:
        print("Impossible")