a, b=map(int, input().split()) # map(bool, input().split()) 로 하면 입력값이 문자열로 취급되어 0도 True로 처리됨
a=bool(a)
b=bool(b)
if a!=b:
    print(1)
else:
    print(0)