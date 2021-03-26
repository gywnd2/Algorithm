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
    # 결과물을 저장할 배열
    res=[]
    # Merge 중간 결과를 저장할 배열
    aux=[]
    # do-While문을 True로 설정한 while과 isInitial 변수로 대체
    while True:
        if isInitial == False:
            # 2씩 증가하는 for문에서 원소 하나씩 슬라이스하여 한 쌍씩 Merge
            for i in range(0, len(arr), 2):
                left = arr[i:i + 1]
                right = arr[i + 1:i + 2]
                # 첫 시행이기 때문에 결과는 바로 res배열에 담겨 else로 전달
                res.append(merge(left, right))
            isInitial = True
        else:
            # 각각의 원소의 크기가 커질 뿐 한 쌍씩 Merge하는 것은 같음
            for i in range(0, len(res), 2):
                # Merge를 진행하다 res배열이 size가 1이 될 경우
                # (정렬이 완료된 하나의 배열을 갖는 경우가 됨.) 반환
                if len(res)==1:
                    return res[0]
                left = res[i]
                # 중간 단계에서 원소가 홀수가 될 경우 index out of range가 발생함
                try:
                    right = res[i + 1]
                # 그래서 짝이 없는 오른쪽 원소는 에러를 발생시키지 않고 바로 Merge 되도록 함
                except:
                    right=[]
                # 한 단계 정렬이 완료된 결과물을 aux에 추가
                aux.append(merge(left, right))
            # 최종 결과물을 담을 res를 aux로 치환
            res=aux
            # 임시 저장공간인 aux를 초기화
            aux=[]

print(bottomTopMergeSort([5,4,3,2,1]))
