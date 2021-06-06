"""
Pseudo code:
    Reversort(L):
    for i := 1 to length(L) - 1
        j := position with the minimum value in L between i and length(L), inclusive
        Reverse(L[i..j])
"""
# 테스트 케이스 수 T 입력
T=int(input())
# 테스트 케이스를 입력받을 빈 리스트 초기화
cases=[[] for _ in range(T)]
# T번 만큼
for i in range(T):
    # map으로 케이스를 입력받을 것이기 때문에 N은 무의미해짐
    N=int(input())
    # 케이스 입력
    cases[i]=list(map(int, input().split()))
# 케이스 번호를 출력해줄 변수 선언 및 초기화
iter=0
for case in cases:
    # 정답을 저장할 변수
    cost=0
    # 1~케이스의 길이-1 까지 반복
    for i in range(1, len(case)):
        # 최솟값을 찾기 위해
        # i 부터 끝까지 슬라이싱
        minValArr=case[i-1:]
        # 슬라이싱된 리스트에서 최솟값의 인덱스 탐색
        j=minValArr.index(min(minValArr))
        # i 부터 최솟값 인덱스 j 까지의 리스트 슬라이싱
        subArr=case[i-1:j+i]
        # 뒤집기 수행
        subArr.reverse()
        # 케이스의 i~j 부분에 subArray를 매핑 시키기 위해 인덱스 선언
        subIdx=0
        for k in range(i-1, j+i+1):
            # subArray를 다 훑으면 break
            if subIdx==len(subArr):
                break
            # 케이스의 i~j 인덱스에 subArray의 값을 하나씩 대응 시킴
            case[k]=subArr[subIdx]
            # subArray 인덱스 증가
            subIdx+=1
        # 구하고자 하는 비용(subArray의 길이) 저장
        cost+=len(subArr)
    # 케이스 번호 증가
    iter+=1
    # 출력
    print("Case #%d: %d"%(iter, cost))

"""
T=int(input())
cases=[[] for _ in range(T)]
for i in range(T):
    N=int(input())
    cases[i]=list(map(int, input().split()))
iter=0
for case in cases:
    cost=0
    origin=case.copy()
    for i in range(1, len(case)):
        sublist=case[i-1:]
        minIdx=case.index(min(sublist))
        j=origin.index(min(sublist))
        case[i-1], case[minIdx]=case[minIdx], case[i-1]
        cost+=(j+1-i+1)
    iter+=1
    print("Case #%d: %d"%(iter, cost))
"""
"""
T=int(input())
cases=[[] for _ in range(T)]
for i in range(T):
    N=int(input())
    cases[i]=list(map(int, input().split()))
iter=0
for case in cases:
    cost=0
    for i in range(1, len(case)):
        sublist=case[i-1:]
        if min(sublist)!=case[i-1]:
            j=case.index(min(sublist))
            costIdx=sublist.index(min(sublist))
            case[i-1], case[j]=case[j], case[i-1]
            cost+=(costIdx+1)
        else:
            cost+=1
    iter+=1
    print("Case #%d: %d"%(iter, cost))

"""