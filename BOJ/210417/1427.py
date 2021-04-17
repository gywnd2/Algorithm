import sys
n=str(sys.stdin.readline())
number=[]
for i in range(len(n)-1):
    number.append(int(n[i]))
def quick(arr, start, end):
    if start>=end:
        return
    pivot=start; l=start+1; r=end
    while l<=r:
        while l <= end and arr[l] > arr[pivot]:
            l += 1
        while r > start and arr[r] <= arr[pivot]:
            r -= 1
        if l>r:
            arr[r], arr[pivot]=arr[pivot], arr[r]
        else:
            arr[l], arr[r]=arr[r],arr[l]
    quick(arr, start, r-1)
    quick(arr, r+1, end)
quick(number, 0, len(number)-1)
result=''
for digit in number:
    result+=str(digit)
print(result)