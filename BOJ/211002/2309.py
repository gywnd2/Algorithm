import itertools
dwarf=[]
for _ in range(9):
    dwarf.append(int(input()))
dwarf=itertools.combinations(dwarf, 7)
for case in dwarf:
    if sum(case)==100:
        case=list(case)
        case.sort()
        for height in case:
            print(height)
        break