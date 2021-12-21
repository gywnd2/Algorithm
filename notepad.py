import random

# 주사위 두개 정의
dice1 = [3,3,3,3,3,3]
dice2 = [1,1,1,1,4,4]

# 주사위 던진 결과 두개
total = 100 
ev = 0

for i in range(1, 101):
    # 주사위 던져 !
    value1 = random.choice(dice1)
    value2 = random.choice(dice2)
    # 1번 주사위가 이기면 (이겨야 결과도 출력됨)
    if value1 > value2: 
        ev = ev+1
        print(i, "번째 시행")
        print("value1 : ", value1, "/", "value2 : ", value2)
        print("승률 : ", ev/total)
        print()
    
    else:
        print(i, "번째 시행")
        print("value1 : ", value1, "/", "value2 : ", value2)
        print("2번 주사위가 졌습니다. ")
        print()