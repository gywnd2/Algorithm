import sys
input=sys.stdin.readline().strip()

n=int(input)
paper=[list(map(int, input())) for _ in range(n)]
print(paper)