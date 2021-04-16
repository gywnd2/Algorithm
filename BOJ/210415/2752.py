num=list(map(int, input().split()))
def selectionSort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1, len(arr)):
            if arr[min]>arr[j]:
                min=j
        arr[min], arr[i]=arr[i],arr[min]
    return arr
num=selectionSort(num)
for n in num:
    print("%d " %n,end='')