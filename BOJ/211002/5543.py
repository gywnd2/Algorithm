burger=[]
drink=[]
order=[]
for _ in range(3):
    burger.append(int(input()))
for _ in range(2):
    drink.append(int(input()))
for i in burger:
    for j in drink:
        order.append(i+j)
print(min(order)-50)