k=int(input())
for i in range(k):
    score=list(map(int, input().split()))
    score=score[1:]
    score.sort(reverse=True)
    gap=0
    for j in range(len(score)-1):
        if score[j]-score[j+1]>gap:
            gap=score[j]-score[j+1]
    print("Class",(i+1))
    print("Max "+str(max(score))+", Min "+str(min(score))+", Largest gap "+str(gap))