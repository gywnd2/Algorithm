n=int(input())
arr=list(int(input()) for _ in range(n))
# arr=sorted(arr, reverse=True)
arr.sort()
arr.reverse()
print(arr)