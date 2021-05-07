paid=int(input())
remainder=1000-paid
coins=[500, 100, 50, 10, 5, 1]; idx=0; count=0
while True:
    while idx<=5:
        if remainder==0:
            break
        if remainder>=coins[idx]:
            count+=(remainder//coins[idx])
            remainder%=coins[idx]
        elif idx<5 and remainder>=coins[idx+1]:
            count+=1
            remainder-=coins[idx+1]
        else:
            idx+=1
    print(count)
    break