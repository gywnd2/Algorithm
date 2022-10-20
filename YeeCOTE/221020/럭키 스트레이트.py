import sys
num=list(sys.stdin.readline().strip())
mid=len(num)//2
left, right=num[:mid], num[mid:]
lSum, rSum=0, 0
for i in range(mid):
    lSum+=int(left[i])
    rSum+=int(right[i])
if lSum==rSum:
    print("LUCKY")
else:
    print("READY")