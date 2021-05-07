import sys
n, k=map(int, sys.stdin.readline().strip().split())
coins=list(int(sys.stdin.readline()) for _ in range(n))
coins.sort(reverse=True); count=0; idx=0
while True:
    # 인덱스는 끝까지
    while idx<=n-1:
        # 큰 동전 부터 거스르기
        if k>=coins[idx]:
            k-=coins[idx]
            count+=1
        # 큰 동전으로 다 거슬렀으면 다음 동전 시도
        else:
            # out of range를 피하기 위한 <n-1 조건 추가
            if idx<n-1 and k>=coins[idx+1]:
                k-=coins[idx+1]
                count+=1; idx+=1
            # 마지막 하나 전 동전까지 왔으면 마지막 동전(1원)시도 
            else:
                idx+=1
    print(count)
    break