"""
dp fibonacci


def binSearch(arr, target):
    l=0; r=len(arr)-1
    while l<=r:
        mid=l+(r-l)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<=target:
            r=mid-1
        else:
            l=mid+1
    return -1

def insertionSort(arr):
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
            else:
                break

def selectionSort(arr):
    for i in range(len(arr)-1):
        min=i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[i], arr[min]=arr[min], arr[i]

def merge(left, right):
    res=[]
    while len(left)>0  or len(right)>0:
        if left[0]<=right[0]:
            res.append(left[0])
            left=left[1:]
        else:
            res.append(right[0])
            right=right[1:]
    while len(left)>0:
        res.append(left[0])
        left=left[1:]
    while len(right)>0:
        res.append(right[0])
        right=right[1:]
    return res

def mergeSort(arr, l, r):
    if len(arr)<=1:
        return
    mid=l+(r-l)//2
    left=arr[:mid]
    right=arr[mid:]
    left=mergeSort(left)
    right=mergeSort(right)
    return merge(left, right)

def quickSort(arr, l, r):
    if l>=r:
        return
    pivot=l; p=l+1; q=r
    while p<=q:
        while p<=r and arr[p]<=arr[pivot]:
            p+=1
        # q가 l과 같아져도 어차피 피벗이기 때문에 상관이 없다.
        # arr[q]>=arr[pivot]이어도 앞의 while문에서
        # 이미 같은 경우가 처리되기 때문에 같은 경우가 안생김
        while q>l and arr[q]>arr[pivot]:
            q-=1
        if p>q:
            arr[q], arr[pivot]=arr[pivot], arr[q]
        else:
            arr[p], arr[q]=arr[q], arr[p]
    quickSort(arr, l, q-1)
    quickSort(arr, q+1, r)

def fiboRecur(num):
    if num<=1:
        return num
    else:
        return fiboRecur(num-1)+fiboRecur(num-2)

def fiboIter(num):
    fib=[0,1]
    for i in range(2, num+1):
        fib.append(num-1); fib.append(num-2)
    return fib

"""

def insertionSort(arr):
    for i in range(len(arr)):
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                arr[j-1], arr[j]=arr[j], arr[j-1]
            else:
                break

def selectionSort(arr):
    for i in range(len(arr)-1):
        min=i
        for j in range(i+1, len(arr)):
            if arr[min]>arr[j]:
                min=j
        arr[i], arr[min]= arr[min], arr[i]

def merge(left, right):
    result=[]
    while len(left)>0 or len(right)>0:
        while len(left)>0 and len(right)>0:
            if left[0]<right[0]:
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
    pivot=start; l=start; r=end
    while l<=end and arr[l]<=arr[pivot]:
        l+=1
    # r
    while r>=start and arr[r]>arr[pivot]:
        r-=1
    if l>r:
        arr[r], arr[pivot]=arr[pivot], arr[r]
    else:
        arr[l], arr[r]=arr[r],arr[l]
    quickSort(arr, start, r-1)
    quickSort(arr, r+1, end)

def binSearch(arr, target):
    l=0; r=len(arr)-1
    while l<=r:
        mid = l + (r - l) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return -1

def threeWayQuick(arr, start, end):
    if start>=end:
        return
    pivot=start; l=start; mid=start; r=end
    while mid<=r:
        if arr[mid]<pivot:
            arr[l],arr[mid]=arr[mid],arr[l]
            l+=1
            mid+=1
        elif arr[mid]>pivot:
            arr[mid], arr[r]=arr[r], arr[mid]
            r-=1
        else:
            mid+=1
    threeWayQuick(arr, start, l-1)
    threeWayQuick(arr, r+1, end)

arr=[5,4,3,2,1]
arr2=[0,1,2,3,4,5,6,7,8,9,10]
print(mergeSort(arr))

import sys
n=int(sys.stdin.readline())
fiboMem=list(0 for _ in range(n+1))
def fibonacci(num):
    if num==1 or num==2:
        fiboMem[num]=1
    elif fiboMem[num]!=0:
        return fiboMem[num]
    else:
        fiboMem[num]=fibonacci(num-1)+fibonacci(num-2)
    return fiboMem[num]
