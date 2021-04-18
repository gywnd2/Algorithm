def binarySearchRecur(arr, key, start, end):
    if start>end:
        return -1
    mid=(start+end)//2
    if arr[mid]==key:
        return mid
    elif arr[mid]<key:
        return binarySearchRecur(arr, key, mid+1, end)
    else:
        return binarySearchRecur(arr, key, start, mid-1)

def binarySearchIter(arr, key, start, end):
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            start=mid+1
        else:
            end=mid-1
    return -1

def selectionSort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[min], arr[i]=arr[i], arr[min]
    return arr

def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j]<arr[j-1]:
                arr[j], arr[j-1]=arr[j-1],arr[j]
            else:
                break 
    return arr

def merge(left, right):
    result=[]
    while len(left)>0 or len(right)>0:
        while len(left)>0 and len(right)>0:
            if left[0]<=right[0]:
                result.append(left[0])
                left=left[1:]
            else:
                result.append(right[0])
                right=right[1:]
        while len(left)>0:
            result.append(left[0])
            left=left[1:]
        while len(right)>0:
            result.append(right[0])
            right=right[1:]
    return result

def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    left=mergeSort(left)
    right=mergeSort(right)
    return merge(left, right)

def quickSort(arr, start, end):
    if start>=end:
        return
    pivot=start; l=start+1; r=end
    while l<=r:
        while l<=end and arr[l]<=arr[pivot]:
            l+=1
        while r>start and arr[r]>arr[pivot]:
            r-=1
        if l>r:
            arr[r], arr[pivot]=arr[pivot], arr[r]
        else:
            arr[l], arr[r]=arr[r], arr[l]
    quickSort(arr, start, r-1)
    quickSort(arr, r+1, end)


def fiboIter(x):
    fib[0]=0; fib[1]=1
    for i in range(2, len(fib)):
        fib[i]=fib[i-1]+fib[i-2]
    print(fib[x])

def fiboRecur(x):
    if x==0 or x==1:
        return x
    else:
        return fiboRecur(x-1)+fiboRecur(x-2)

def fiboDP(x):
    fib[0]=0; fib[1]=1
    if fib[x]!=-1:
        return fib[x]
    else:
        fib[x]=fiboDP(x-1)+fiboDP(x-2)
        return fib[x]

def threeWayQuick(arr, start, end):
    if start>=end:
        return 
    pivot=arr[start]; l=start; r=end; mid=start
    while  mid<=r:
        if arr[mid]<pivot:
            arr[l], arr[mid]=arr[mid], arr[l]
            l+=1
            mid+=1
        elif arr[mid]>pivot:
            arr[r], arr[mid]=arr[mid], arr[r]
            r-=1
        else:
            mid+=1
    threeWayQuick(arr, start, l-1)
    threeWayQuick(arr, r+1, end)

fib=[-1 for _ in range(10001)]
arr=[1,2,3,4,5,6,7,8,9]
arr2=[6,3,8,5,2,2,9,9,5,4,8,4,2]
quickSort(arr2, 0, len(arr2)-1)
#print(arr2)
#fiboIter(50)
#print(fiboRecur(40))
print(fiboDP(20))
threeWayQuick(arr2, 0, len(arr2)-1)
print(arr2)