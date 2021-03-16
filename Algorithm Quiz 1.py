def checkAsc(arr, N):
    res=True
    idx=1
    while idx!=N:
        for i in range(1, N):
            idx+=1
            if arr[i - 1] > arr[i]:
                res = False
                break
    return res

num=[1,3,2,4,5]
print(checkAsc(num, 5))