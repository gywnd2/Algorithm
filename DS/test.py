def mergeSort(a):
    if len(list)<=1:
        return list
    mid=len(list)//2
    leftHalf=list[:mid]
    rightHalf=list[mid:]
    leftHalf=mergeSort(leftHalf)
    rightHalf=mergeSort(rightHalf)
    return merge(leftHalf, rightHalf)

def merge(left, right):
    sortedArr=[]
    while len(left)>0 or len(right)>0:
        if len(left)>0 and len(right)>0:
            if left[0]<=right[0]:
                sortedArr.append(left[0])
                left=left[1:]
            else:
                sortedArr.append(right[0])
                right=right[1:]
        elif len(left)>0:
            sortedArr.append(left[0])
            left=left[1:]
        elif len(right)>0:
            sortedArr.append(right[0])
            right=right[1:]
    return sortedArr

def bottomTopMergeSort(arr):
    isInitial=False
    res=[]
    aux=[]
    while True:
        if isInitial == False:
            for i in range(0, len(arr), 2):
                left = arr[i:i + 1]
                right = arr[i + 1:i + 2]
                res.append(merge(left, right))
            isInitial = True
        else:
            for i in range(0, len(res), 2):
                print("in i:", i)
                print("res",res)
                if len(res)==1:
                    return res[-1]
                left = res[i]
                print("left", left)
                right = res[i+1]
                print("right", right)
                aux.append(merge(left, right))
            res=aux
            aux=[]

print(bottomTopMergeSort([5,4,3,2,1,0]))
