import sys
def binSearch(start, end):
    global maxLen, maxSum, arr
    while start<=end:
        tmp=0
        # print('maxLen :',maxLen, 'maxSum :',maxSum, 'start :',start,'end :',end, 'tmp :',tmp)
        mid=(start+end)//2
        for i in arr:
            # print('i :', i, 'arr[mid]:', arr[mid])
            if i-arr[mid]>0:
                tmp+=i-arr[mid]
        if tmp<M:
            end=mid-1
        else:
            maxLen=arr[mid]
            start=mid+1

N, M=map(int, sys.stdin.readline().rstrip().split())
arr=list(map(int, sys.stdin.readline().rstrip().split()))
maxLen=0
arr.sort()
binSearch(0, N-1)
print(maxLen)

