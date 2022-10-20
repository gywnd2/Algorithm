import sys
n=int(sys.stdin.readline().strip())
adv=list(map(int, sys.stdin.readline().strip().split()))
adv.sort(reverse=True)
count=0
while True:
    if len(adv)<adv[0]:
        break
    if len(adv)==adv[0]:
        print(count+1)
        break
    adv=adv[adv[0]:]
    count+=1