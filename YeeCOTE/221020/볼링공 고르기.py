N, M=map(int, input().split())
balls=list(map(int, input().split()))
balls.sort()

result=0
for i in range(N):
    for j in range(i, N):
        if balls[i]!=balls[j]:
            result+=1

print(result)