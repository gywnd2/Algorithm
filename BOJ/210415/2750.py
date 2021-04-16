import sys
t=int(sys.stdin.readline())
n=list(int(sys.stdin.readline()) for _ in range(t))
def insertionSort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, 0, -1):
            if arr[j]<arr[j-1]:
                arr[j], arr[j-1]=arr[j-1], arr[j]
            else:
                break
    return arr
n=insertionSort(n)
for num in n:
    print(num)