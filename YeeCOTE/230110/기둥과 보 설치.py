# 기둥은 바닥 위에 있거나
# 보의 한쪽 끝 부분 위에 있거나, 
# 또는 다른 기둥 위에 있어야 합니다.

# 보는 한쪽 끝 부분이 기둥 위에 있거나,
# 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
def solution(n, build_frame):
    answer = []
    for order in build_frame:
        x, y, isBeam, install=order
        if install:                
            answer.append((x, y, isBeam))
            for frame in answer:
                if not check(frame[0], frame[1], frame[2], answer):
                    answer.remove((x, y, isBeam))
                    break
                # print("added!!", answer)
        
        # 삭제할 경우
        else:
            answer.remove((x, y, isBeam))
            for frame in answer:
                if not check(frame[0], frame[1], frame[2], answer):
                    answer.append((x, y, isBeam))
                    break
            
    answer.sort(key=lambda x:(x[0], x[1], x[2]))
    # print(answer)
    return answer

def check(x, y, isBeam, answer):
    # 보일 경우
    if isBeam:
        # 기둥이 맞닿아 있을 경우
        if (x, y-1, 0) in answer or (x+1, y-1, 0) in answer:
            pass
        # 양쪽에 보가 있을 경우:
        elif (x-1, y, 1) in answer and (x+1, y, 1) in answer:
            pass
        else:
            return False
            
    # 기둥일 경우
    else:
        if y==0:
            pass
        elif (x-1, y, 1) in answer or (x, y, 1) in answer:
            pass
        elif (x, y-1, 0) in answer:
            pass
        else:
            return False
            
    return True

solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])