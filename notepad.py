import sys
t=int(sys.stdin.readline())
for _ in range(t):
    n=int(sys.stdin.readline()); score=[]
    scorea=0; scoreb=0
    for _ in range(n):
        a, b=sys.stdin.readline().split()
        score.append([int(a),float(b)])
    for subject in score:
        scorea+=subject[0]
        scoreb+=subject[1]
    print(scorea, scoreb)