price, count, balance=map(int, input().split())
if price*count-balance<0:
    print(0)
else:
    print(price*count-balance)