import sys
n=int(sys.stdin.readline().strip())
num=[]
for _ in range(n):
    num.append(int(sys.stdin.readline().strip()))

def selectionSort(arr):
    for i in range(n-1):
        for j in range(i, n):
            if arr[i]>arr[j]:
                arr[i], arr[j]=arr[j], arr[i]
selectionSort(num)
print(num)
                
# 기본 정렬 라이브러리 사용
# print(sorted(num))