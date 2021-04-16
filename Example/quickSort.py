def quickSort(arr, l, r):
    if l>=r:
        return arr
    pivot=l; p=l+1; q=r
    while p<=q:
        while p<=r and arr[p]<=arr[pivot]:
            p+=1
        while q>l and arr[q]>arr[pivot]:
            q-=1
        if p>q:
            arr[q], arr[pivot]=arr[pivot], arr[q]
        else:
            arr[p], arr[q]=arr[q], arr[p]
    quickSort(arr, l, q-1)
    quickSort(arr, q+1, r)

arr=[10,1,5,8,7,6,4,3,2,9]
quickSort(arr, 0, len(arr)-1)
print(arr)