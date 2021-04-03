def QuickSort(arr, first, last):
    # first와 last가 만나거나 엇갈릴경우 = 정렬 완료
    if first>=last:
        return
    # 피봇과 좌한계, 우한계 설정
    pivot=first
    left=first+1
    right=last
    # 좌한계와 우한계가 아직 만나거나 엇갈리지 않았다면 = 정렬 미완료
    while left<=right:
        # 좌한계가 배열의 끝에 도달하지 않았고 피봇값보다 작은 값들이라면
        while left<=last and arr[left]<=arr[pivot]:
            left+=1
        # 우한계가 배열의 처음에 도달하지 않았고 피봇값보다 큰 값들이라면
        while right>first and arr[right]>=arr[pivot]:
            right-=1
        # 만약 좌한계 우한계가 엇갈리면 작은 값을 피봇과 교환
        if left>right:
            arr[right],arr[pivot]=arr[pivot],arr[right]
        # 엇갈리지 않았다면 정상적으로 작은값과 큰값을 교환
        else:
            arr[left],arr[right]=arr[right], arr[left]
    QuickSort(arr, first, right-1)
    QuickSort(arr, right+1, last)

arr=[5,7,9,0,3,1,6,2,4,8]
QuickSort(arr,0,len(arr)-1)
print(arr)


