vColor=[]; W=[[]]
def mColoring(i):
    if promising(i):
        if i==n:
            print(vColor)
        else:
            for color in range(2, m):
                vColor.append(color)
                mColoring(i)

def promising(i):
    j=1; switch=true
    while j<i and switch:
        if W[i][j] and vColor[i]==vColor[j]:
            switch=False
        j+=1
    return switch