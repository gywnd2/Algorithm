import sys
a, b, v=map(int, sys.stdin.readline().split())
res=(v-b)/(a-b)
if (int(res)!=res):
    print(int(res)+1)
else :
    print(int(res))