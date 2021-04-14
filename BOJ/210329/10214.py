t=int(input())
score=[0,0]
for _ in range(t):
    for _ in range(9):
        y, k = map(int, input().split())
        if y != 0:
            score[0] += y
        if k != 0:
            score[1] += k
    if score[0] > score[1]:
        print("Yonsei")
    elif score[0] < score[1]:
        print("Korea")
    else:
        print("Draw")