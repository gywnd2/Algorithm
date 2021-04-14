def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j]<arr[j-1]:
                arr[j], arr[j-1]=arr[j-1], arr[j]
            else:
                break

arr=[0,2,1,0,887,2,1,2,342421,0,563,0,0,1]
insertionSort(arr)
print(arr)