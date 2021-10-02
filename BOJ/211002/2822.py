score=[-1]*10
for i in range(1, 9):
    score[i]=int(input())
origin=score.copy()
score.sort(reverse=True)
qnum=[]
for i in range(5):
    qnum.append(origin.index(score[i]))
qnum.sort()
print(sum(score[:5]))
print(qnum[0],qnum[1],qnum[2],qnum[3],qnum[4])
