import sys
n=int(sys.stdin.readline().strip())
parts=list(map(int, sys.stdin.readline().strip().split()))
m=int(sys.stdin.readline().strip())
order=list(map(int, sys.stdin.readline().strip().split()))

def binSearch(start, end, target):
    if start>end:
        return 'no'
    mid=(start+end)//2
    # print(mid, parts[mid])
    if parts[mid]==target:
        return 'yes'
    if parts[mid]<target:
        return binSearch(mid+1, end, target)
    if parts[mid]>target:
        return binSearch(start, mid-1, target)
parts.sort()
for i in order:
    print(binSearch(0, n-1, i))