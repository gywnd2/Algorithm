n=int(input())
grade=list(map(int, input().split()))
score=[0 for _ in range(n)]
for i in range(len(grade)):
    if i>0:
        if grade[i]==1 and score[i-1]!=0:
            score[i]+=(score[i-1]+1)
        elif grade[i]==1 and score[i-1]==0:
            score[i]+=1
    else:
        if grade[i]==1:
            score[i]+=1
print(sum(score))