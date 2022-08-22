import sys
input=sys.stdin.readline().strip()

def func(n, r, c):
    if n==0:
        return 0
    mid=2**(n-1)
    # 1 사분면
    if r<mid and c<mid :
        return func(n-1, r, c)
    # 2 사분면
    elif r<mid and c>=mid:
        return mid*mid+func(n-1, r, c-mid)
    # 3 사분면
    elif r>=mid and c<mid:
        return 2*mid*mid+func(n-1, r-mid, c)
    # 4 사분면
    elif r>=mid and c>=mid:
        return 3*mid*mid+func(n-1, r-mid, c-mid)

n, r, c=map(int, input.split())
print(func(n, r, c))