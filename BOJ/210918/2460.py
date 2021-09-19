total=0
history=[]
for _ in range(10):
    off, on=map(int, input().split())
    total-=off; total+=on
    history.append(total)
print(max(history))