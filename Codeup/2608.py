import itertools
n=int(input())
res=list(itertools.product((["O","X"]), repeat=n))
for i in range(0,len(res)):
    for j in range(0, n):
        print(res[i][j],end='')
    print("")