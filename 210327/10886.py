n=int(input())
cute={"1":0, "0":0}
for _ in range(n):
    cute[input()]+=1
if max(cute, key=cute.get)=="1":
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")