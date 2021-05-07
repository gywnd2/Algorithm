def binSearchIter(arr, key):
    l=0; r=len(arr)-1; mid=l+(r-l)//2
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

def selectionSort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[min], arr[i]=arr[i], arr[min]

def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j]<arr[j-1]:
                arr[j], arr[j-1]=arr[j-1], arr[j]
            else:
                break

def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    left=mergeSort(left)
    right=mergeSort(right)
    mergeSort(left)
    mergeSort(right)
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

def threeWayQuick(arr, start, end):
    if start>=end:
        return
    pivot=arr[start]; l=start; mid=start+1; r=end
    while mid<=r:
        if arr[mid]<pivot:
            arr[mid], arr[l]=arr[l], arr[mid]
            l+=1
            mid+=1
        elif arr[mid]>pivot:
            arr[mid], arr[r]=arr[r], arr[mid]
            r-=1
        else:
            mid+=1
    threeWayQuick(arr, start, l-1)
    threeWayQuick(arr, r+1, end)

def fibIter(x):
    fib=[0 for _ in range(x+1)]; fib[0]=0; fib[1]=1
    for i in range(2, len(fib)):
        fib[i]=fib[i-1]+fib[i-2]
    return fib[x]

def fibRecur(x):
    if x<=1:
        return x
    else:
        return fibRecur(x-1)+fibRecur(x-2)

def fibDP(x):
    if fibMem[x]!=-1:
        return fibMem[x]
    else:
        fibMem[x]=fibDP(x-1)+fibDP(x-2)
        return fibMem[x]

def recursiveChange(money, count):
    if money==0:
        return count
    else:
        if money>=coins[0]:
            return min(recursiveChange(money-coins[0], count+1),
                        recursiveChange(money-coins[1], count+1),
                        recursiveChange(money-coins[2], count+1))
        elif money>=coins[1]:
            return min(recursiveChange(money-coins[1], count+1),
                        recursiveChange(money-coins[2], count+1))
        elif money>=coins[2]:
            return recursiveChange(money-coins[2], count+1)    

def dpChange(money, coins):
    changes=[0 for _ in range(money+1)]; changes[6]=1; changes[5]=1; changes[1]=1
    for m in range(1, money+1):
        for coin in coins:
            # 금액이 동전보다 크고 단위 동전이 아니라면
            if m>=coin and changes[m]!=1:
                minCoins=changes[m-coin]+1
                # 계산 된적이 없거나 더 작은 갯수가 나왔다면
                if changes[m]==0 or minCoins<changes[m]:
                    changes[m]=minCoins        
    return changes[m]
                        
coins=[6, 5, 1]
fibMem=[-1 for _ in range(1001)]; fibMem[0]=0; fibMem[1]=1
arr=[6,3,8,5,2,2,9,9,5,4,8,4,2,234342342344,12312242,23,242377887867,2342342352341242]
print(dpChange(50, coins))