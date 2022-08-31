import sys

n, m=map(int, sys.stdin.readline().strip().split())
office=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
print(office)