n=int(input())

result=0
for _ in range(n):
    word=list(input())
    string=list()
    for char in word:
        if len(string)!=0 and char==string[-1]:
            string.pop()
        else:
            string.append(char)
    if len(string)==0:
        result+=1
print(result)