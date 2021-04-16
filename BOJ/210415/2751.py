import sys
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
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    while len(left) > 0:
        result.append(left[0])
        left = left[1:]
    while len(right) > 0:
        result.append(right[0])
        right = right[1:]
    return result

n=int(sys.stdin.readline())
num=list(int(sys.stdin.readline()) for _ in range(n))
print(mergeSort(num))