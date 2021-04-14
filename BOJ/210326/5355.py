n=int(input())
for _ in range(n):
    exp=input().split()
    num=float(exp[0])
    for digit in exp:
        if digit == "@":
            num*=3
        elif digit == "%":
            num+=5
        elif digit == "#":
            num-=7
    print("%.2f" %num)