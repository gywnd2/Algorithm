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

def quickSort2(arr, start, end):
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
    print(arr)

arr=[10,1,5,8,7,6,4,3,2,9]
quickSort2(arr, 0, len(arr)-1)