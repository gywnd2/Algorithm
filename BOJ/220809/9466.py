from collections import deque
import sys
sys.setrecursionlimit(10**8)

def dfs(x):
    visited[x]=1
    tmp.append(x)
    
    nx=students[x]-1
    if not visited[nx]:
        dfs(nx)
    elif nx in tmp:
        team.extend(tmp[tmp.index(nx):])
    

t=int(sys.stdin.readline().strip())
for _ in range(t):
    n=int(sys.stdin.readline().strip())
    students=list(map(int, sys.stdin.readline().strip().split()))   
    team=[]
    visited=[0 for _ in range(n)]
    
    for i in range(n):
        if not visited[i]:
            tmp=[]
            dfs(i)
    
    print(n-len(team))