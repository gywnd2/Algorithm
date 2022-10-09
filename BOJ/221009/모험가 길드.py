import sys
n=int(sys.stdin.readline().strip())
adventurer=list(map(int, sys.stdin.readline().strip().split()))

adventurer.sort(reverse=True)
count=0
while True:
    if len(adventurer)<1:
        break
    num=adventurer[0]
    if len(adventurer)>=num:
        adventurer=adventurer[num:]
        count+=1
    else:
        break

print(count)