def recursiveChange(money, count):
    for coin in coins:
        if money>=coin:
            return recursiveChange(money-coin, count+1)
    print("Minimum number of coins :", count)

coins=[6, 5, 1]
recursiveChange(9,0)