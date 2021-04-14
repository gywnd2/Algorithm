t=int(input())
case=list()

for i in range(t):
    line=input().rstrip()
    case.append(line)

for i in range(len(case)):
    oCount = 0
    score = 0
    for j in range(len(case[i])):
        if case[i][j] == "O":
            oCount += 1
            score += oCount
        else:
            oCount = 0
            pass
    print(score)
    oCount=0
    score=0