import sys

n=int(sys.stdin.readline().strip())
tower=[i for i in range(1, n+1)]
def hanoi(a, b, n):
    if n==1:
        print(a, b)
        return
    else:
        hanoi(a, 6-a-b, n-1)
        print(a, b)
        hanoi(6-a-b, b, n-1)
print(2**n-1)
hanoi(1, 3, n)