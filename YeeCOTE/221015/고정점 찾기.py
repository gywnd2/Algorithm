import sys
from bisect import bisect_left, bisect_right
n=int(sys.stdin.readline().strip())
num=list(map(int, sys.stdin.readline().strip().split()))

def binSearch(start, end):
    if start>end:
        return -1
    mid=(start+end)//2
    if num[mid]==mid:
        return mid
    elif num[mid]>mid:
        return binSearch(start, mid-1)
    elif num[mid]<mid:
        return binSearch(mid+1, end)
    
    
res=binSearch(0, n-1)
if res==-1:
    print(-1)
else:
    print(res)