from collections import deque
import sys

# 뒤집기 체크
reverse = False
# error가 true면 32행의 결과 출력 부분은 실행하지 않도록
error= False

t = int(sys.stdin.readline().strip())

for _ in range(t):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    string = deque(sys.stdin.readline().strip()[1:-1].split(","))

    # 원소 개수가 0이면 deque 비우기
    if n == 0:
        string = deque()

    # p에서 한 글자씩 반복문 실행
    for i in p:
        # D가 나오기 전까지 R이 홀/짝 체크
        # 홀이면 뒤집도록
        if i == "R":
            reverse = not reverse
        # D가 나왔을 경우
        else:
            try:
                # R이 홀수면
                if reverse:
                    string.pop()
                    # R의 홀/짝 다시 세기
                    # reverse = False
                else:                    
                    # 첫 번째 수 버리기
                    string.popleft()
                
            # 원소가 0개면
            except:
                print("error")
                error=True
                break
    
    # 오류가 발생하지 않았으면
    if not error:
        # D 이후 남은 R의 개수가 홀수 였다면
        if reverse:
            string.reverse()
        print("["+",".join(string)+"]")
    # 에러확인 플래그 초기화
    reverse=False
    error=False