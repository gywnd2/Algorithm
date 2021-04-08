def selectionSort(arr):
    for i in range(len(arr)-1):
        min=i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

arr=[5,7,9,0,3,1,6,2,4,8]
selectionSort(arr)
print(arr)