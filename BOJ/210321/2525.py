import time
h, m =map(int, input().split())
c=int(input())
tm = time.gmtime(h*60*60+m*60+c*60)
print(tm.tm_hour,tm.tm_min)