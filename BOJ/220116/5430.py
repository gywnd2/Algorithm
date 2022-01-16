from collections import deque
import sys

reverse = False
isReversed = False
t = int(sys.stdin.readline().strip())
for _ in range(t):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    string = deque(sys.stdin.readline().strip()[1:-1].split(","))
    if n < 1:
        print("error")
        continue

    for i in range(len(p)):
        if p[i] == "R":
            reverse = not reverse
        else:
            try:
                if reverse == True and isReversed == False:
                    string.reverse()
                    isReversed = True
                string.popleft()
            except:
                print("error")
                break

    if isReversed == False and reverse == True:
        string.reverse()

    if len(string) != 0:
        print("["+",".join(string)+"]")
