import sys
n, m=map(int, sys.stdin.readline().strip().split())
d=list(map(int, sys.stdin.readline().strip().split()))
res=[]
def binSearch(start, end):
    # start==end는 안됨!
    if start>end:
        return
    total=0
    mid=(start+end)//2
    # print('mid :',mid)
    for i in d:
        tmp=i-mid
        if tmp>=0:
            total+=tmp
    
    if total>=m:
        res.append(mid)
        binSearch(mid+1, end)
    else:
        binSearch(start, mid-1)

binSearch(0, max(d))
print(max(res))
