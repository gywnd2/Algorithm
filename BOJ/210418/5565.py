import sys
total=int(sys.stdin.readline())
books=[int(sys.stdin.readline()) for _ in range(9)]
print(total-sum(books))