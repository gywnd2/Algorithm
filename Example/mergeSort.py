def merge(left, right):
    result=[]
    while len(left)>0 or len(right)>0:
        if len(left)>0 and len(right)>0:
            if left[0]<=right[0]:
                result.append(left[0])
                left=left[1:]
            else:
                result.append(right[0])
                right=right[1:]
        elif len(left)>0:
            result.append(left[0])
            left=left[1:]
        elif len(right)>0:
            result.append(right[0])
            right=right[1:]
    return result

def mergeSort(arr):
    if len(arr)<=1:
        return
    mid=len(arr)//2
    leftList=arr[:mid]
    rightList=arr[mid:]
    leftList=mergeSort(leftList)
    rightList=mergeSort(rightList)
    return merge(leftList, rightList)