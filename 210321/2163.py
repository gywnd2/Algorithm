n, m=map(int, input().split())
count=0
chocolate=list(list(1 for _  in range(m)) for _ in range(n))
dish=list()
for bigHalf in chocolate:
    for smallHalf in bigHalf:
        count+=1
print(count-1)
