import sys

test=int(input())
for _ in range(test):
    a, b=map(int, sys.stdin.readline().split())
    print(a+b)