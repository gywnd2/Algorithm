def solution(numbers, hand):
    answer = ''
    keypad=[1,2,3,4,5,6,7,8,9,10,0,11]
    lPosition=10; rPosition=11
    target=[]
    for digit in numbers:
        if digit in {1, 4, 7}:
            answer+="L"
            lPosition=digit
        elif digit in {3, 6, 9}:
            answer+="R"
            rPosition=digit
        else:
            for i in range(len(keypad)):
                print(digit, keypad[i])
                if lPosition in keypad[i]:
                    lPosition=[i, keypad[i].index(lPosition)]
                elif rPosition in keypad[i]:
                    rPosition=[i, keypad[i].index(rPosition)]
                elif digit in keypad[i]:
                    print(digit, keypad[i])
                    target=[i, keypad[i].index(digit)]
                lDiff=abs(target[0]-lPosition[0])+abs(target[1]-lPosition[1])
                rDiff=abs(target[0]-rPosition[0])+abs(target[1]-rPosition[1])
                if lDiff < rDiff:
                    answer += "L"
                elif lDiff > rDiff:
                    answer += "R"
                else:
                    if hand == "left":
                        answer += "L"
                    elif hand == "right":
                        answer += "R"

    return answer
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))