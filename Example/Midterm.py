def binSearchIter(arr, key):
    l=start; r=len(arr)-1
    while l<=r:
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            l=mid+1
        else:
            r=mid-1
    return -1

def binSearchRecur(arr, key, start, end):
    if start>end:
        return -1
    else:
        mid=start+(end-start)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            return binSearchRecur(arr, key, mid+1, end)
        else:
            return binSearchRecur(arr, key, start, mid-1)


def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr)):
            if arr[j]<arr[j-1]:
                arr[j], arr[j-1]=arr[j-1], arr[j]
            else:
                 break

def selectionSort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i, 0, -1):
            if arr[min]>arr[j]:
                min=j
        arr[min], arr[i]=arr[i], arr[min]

def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    left=mergeSort(left)
    right=mergeSort(right)
    return merge(left, right)        
    
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

def quickSort(arr,start, end):
    if start>=end:
        return
    pivot=start; l=start+1; r=end
    while l<=r:
        while l<=end and arr[l] <= arr[pivot]:
            l+=1
        while r>start and arr[r] > arr[pivot]:
            r-=1
        if l>r:
            arr[r], arr[pivot]=arr[pivot], arr[r]
        else:
            arr[l], arr[r]=arr[r], arr[l]
    quickSort(arr, start, r-1)
    quickSort(arr, r+1, end)

def threeWayQuick(arr, start, end):
    if start>=end:
        return
    pivot=arr[start]; l=start; mid=start+1; r=end
    while mid<=r:
        if arr[mid]<=pivot:
            arr[l], arr[mid]=arr[mid], arr[l]
            mid+=1
            l+=1
        elif arr[mid]>pivot:
            arr[r], arr[mid]=arr[mid], arr[r]
            r-=1
        else:
            mid+=1
    threeWayQuick(arr, start, l-1)
    threeWayQuick(arr, r+1, end)

fib=[-1 for _ in range (101)];fib[0]=0;fib[1]=1
def fibDP(x):
    if fib[x]!=-1:
        return fib[x]
    else:
        fib[x]=fibDP(x-2)+fibDP(x-1)
        return fib[x]

#O(n)
def fibIter(x):
    fibMem=[0 for _ in range(x+1)]
    fibMem[0]=0; fibMem[1]=1
    if x<=1:
        return fibMem[x]
    else:
        for i in range(2, len(x)+1):
            fibMem[i]=fibMem[i-1]+fibMem[i-2]
    return fibMem[x]

# O(2^n/2)
def fibRecur(x):
    if x<=1:
        return x
    else:
        return fibRecur(x-1)+fibRecur(x-2)

coins=[6,5,1]
def recursiveChange(money, count):
    if money==0:
        return count
    else:
        if money>=coins[0]:
            return min(recursiveChange(money-coins[0], count+1),
                       recursiveChange(money-coins[1], count+1),
                       recursiveChange(money-coins[2], count+1))
        elif money>=coins[1]:
            return min(recursiveChange(money-coins[2], count+1),
                       recursiveChange(money-coins[1], count+1))
        elif money>=coins[2]:
            return recursiveChange(money-coins[2], count+1)

def dpChange(money, coins):
    change=[0 for _ in range(100)]
    change[6]=1; change[5]=1; change[1]=1
    for m in range(1, money+1):
        for coin in coins:
            if m>=coin and change[m]!=1:
                numCoins=change[m-coin]+1
                if change[m]==0 or numCoins<change[m]:
                    change[m]=numCoins
    return change[m]


#Driver code
coins=[5,6,1]
fib=[-1 for _ in range(10001)]; fib[0]=0; fib[1]=1
arr=[1,2,3,4,5,6,7,8,9]
arr2=[6,3,8,5,2,2,9,9,5,4,8,4,2,234342342344,12312242,23,242377887867,2342342352341242]
quickSort(arr2, 0, len(arr2)-1)
print(arr2)