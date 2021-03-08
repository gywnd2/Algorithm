t=int(input())
case=list()
for _ in range(t):
    line=input().split()
    line=list(map(int, line))
    case.append(line)

for i in range(t):
    avg=(sum(case[i])-case[i][0])/(len(case[i])-1)
    count=0
    for j in range(1, len(case[i])):
        if case[i][j]>avg:
            count+=1

    print("%0.3f%%" %((count/case[i][0])*100))