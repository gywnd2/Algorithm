t=int(input())
count=0
while True:
    if count==t:
        break
    num=int(input())
    school=list(list(input().split()) for _ in range(num))
    schoolDict={school[i][1]:int(school[i][0]) for i in range(num)}
    print(max(schoolDict, key=schoolDict.get))
    count+=1