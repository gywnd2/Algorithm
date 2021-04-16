import sys
n=int(sys.stdin.readline())
sol=[0 for _ in range(1000001)]
sol[2]=1; sol[3]=1
for i in range(1, len(sol)):
    if sol[i]!=1:
        if i>=3 and i%3==0:
            if i%2==0:
                sol[i] = min(sol[i - 1], sol[i // 2], sol[i // 3]) + 1
            else:
                sol[i] = min(sol[i - 1], sol[i // 3]) + 1
        elif i>=2 and i%2==0:
            sol[i] = min(sol[i - 1], sol[i // 2]) + 1
        else:
            if i==1:
                continue
            sol[i] = sol[i-1] + 1
print(sol[n])