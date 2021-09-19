total=0
history=[]
for _ in range(4):
    off, on=map(int, input().split())
    total+=on; total-=off
    history.append(total)
print(max(history))