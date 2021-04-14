import datetime
n=int(input())
people={}
for _ in range(n):
    inputList=input().split()
    d=datetime.date(int(inputList[3]),int(inputList[2]),int(inputList[1]))
    people[inputList[0]]=d.toordinal()
print(max(people, key=people.get))
print(min(people, key=people.get))