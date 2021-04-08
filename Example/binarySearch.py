def binSearch(arr, target):
    l=0; r=len(arr)-1
    while l<=r:
        mid=l+(r-l)//2
        if arr[mid]==target:
            return mid
        elif target<arr[mid]:
            r=mid-1
        else:
            l=mid+1
    return -1

arr=[0,1,2,3,4,5,6,7,8,9,10]
print(binSearch(arr, 5))