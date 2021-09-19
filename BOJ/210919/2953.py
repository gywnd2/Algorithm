competitor=[]
for _ in range(5):
    score=list(map(int, input().split()))
    competitor.append(sum(score))
print(competitor.index(max(competitor))+1, max(competitor))