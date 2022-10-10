import sys
n=int(sys.stdin.readline().strip())
count=0
for n in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(n)+str(m)+str(s):
                count+=1
print(count)