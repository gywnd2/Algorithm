import sys
n=int(sys.stdin.readline().strip())
students=[list(sys.stdin.readline().strip().split()) for _ in range(n)]
sort={}
for name, score in students:
    sort[score]=name
for score in sorted(list(sort.keys())):
    print(sort[score], end=' ')