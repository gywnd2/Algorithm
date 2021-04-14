import time
h, m, s=map(int, input().split())
c=int(input())
tm = time.gmtime(h*60*60+m*60+c+s)
print(tm.tm_hour,tm.tm_min, tm.tm_sec)