"""
def recursiveChange(money, count):
    for coin in coins:
        if money>=coin:
            return recursiveChange(money-coin, count+1)
    print("Minimum number of coins :", count)


recursiveChange(9,0)
"""
coins=[6,5,1]
def dpChange(money, coins):
    # 결과를 저장할 배열 생성
    minNumCoins=[0 for _ in range(100)]
    # 0부터 money까지의 숫자를 다 돌면서 최소 갯수 계산
    for m in range(0, money+1):
        # 각 m에서 주어진 동전으로 거스를 수 있는지 확인
        for i in range(0, len(coins)):
            # 금액이 동전 액면가보다 크면
            # coins가 정렬되어 있으므로 Greedy 하게 계산함
            if m>= coins[i]:
                # m에서 그 동전으로 거스르고 +1 하여 numCoins로 저장
                numCoins=minNumCoins[m-coins[i]]+1
                # 가장 액면가가 큰 동전으로 이미 계산 되었다면 pass
                if minNumCoins[m]==0:
                    minNumCoins[m]=numCoins
    return minNumCoins[m]

print(dpChange(9, coins))