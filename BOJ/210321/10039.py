avgScore=list(int(input()) for _ in range(5))
sum=0
for s in avgScore:
    if s <40:
        sum+=40
    else:
        sum+=s
print("%d" %(sum/len(avgScore)))