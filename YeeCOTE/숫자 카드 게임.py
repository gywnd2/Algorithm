N, M=map(int, input().split())
cards=[]; minCards=[]
for _ in range(N):
    line=list(map(int, input().split()))
    cards.append(line)
for line in cards:
    minCards.append(min(line))
print(max(minCards))