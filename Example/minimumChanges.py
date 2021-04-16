"""
def recursiveChange(money, count):
    for coin in coins:
        if money>=coin:
            return recursiveChange(money-coin, count+1)
    print("Minimum number of coins :", count)

recursiveChange(9,0)

"""
coins=[5, 6, 1]
def recursiveChange(money, count):
    if money==0:
        return count

    if money>=coins[0]:
        return recursiveChange(money-coins[0], count+1)
    elif money>=coins[1]:
        return recursiveChange(money-coins[1], count+1)
    else:
        return recursiveChange(money-coins[2], count+1)


print(recursiveChange(23,0))


def dpChange(money, coins):
    # 결과를 저장할 배열 생성
    minNumCoins=[0 for _ in range(100)]
    minNumCoins[6]=1; minNumCoins[5]=1; minNumCoins[1]=1
    # 0부터 money까지의 숫자를 다 돌면서 최소 갯수 계산
    for m in range(1, money+1):
        # 각 m에서 주어진 동전으로 거스를 수 있는지 확인
        for i in range(0, len(coins)):
            # 금액이 동전 액면가보다 크고 6, 5, 1 중 하나가 아니라면
            if m>= coins[i] and minNumCoins[m]!=1:
                # 7을 5로 거스르고 남은 2를 거스르는 방법은 이미 계산된 것을 가져온다.
                numCoins=minNumCoins[m-coins[i]]+1
                # 처음 계산된 값이거나 이미 계산된 갯수보다 적은 갯수가 나왔다면 갱신
                if minNumCoins[m]==0 or numCoins<minNumCoins[m]:
                    minNumCoins[m]=numCoins
    return minNumCoins[m]

print(dpChange(23, coins))