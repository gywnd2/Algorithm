import sys
cards=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for _ in range(10):
    a, b=map(int, sys.stdin.readline().strip().split())
    rList=cards[a:b+1]
    rList.reverse()
    cards[a:b+1]=rList
for i in range(1, 21):
    print(cards[i], end=' ')