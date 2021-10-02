import itertools
num=list(int(input()) for _ in range(9))
num=itertools.combinations(num, 7)
for case in num:
    if sum(case)==100:
        for i in case:
            print(i)