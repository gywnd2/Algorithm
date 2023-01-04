from collections import deque 
import sys, copy
N=int(sys.stdin.readline().strip())
graph=[[] for _ in range(N+1)]
indegree=[0]*(N+1)
time=[0]*(N+1)
for i in range(1, N+1):
    data=list(map(int, sys.stdin.readline().strip().split()))
    time[i]=data[0]
    for x in data[1:-1]:
        indegree[i]+=1
        graph[x].append(i)
    
    # tmp=list(map(int, sys.stdin.readline().strip().split()))[:-1]
    # time[i]=tmp[0]
    # graph[i]=tmp[1:]
    # if len(graph[i])>0:
    #     indegree[i]+=len(graph[i])
    # else:
    #     indegree[i]=0
    
def topology_sort():
    result=copy.deepcopy(time)
    q=deque()
    
    for i in range(1, N+1):
        if indegree[i]==0:
            q.append(i)
    
    while q:
        now=q.popleft()
        for i in graph[now]:
            result[i]=max(result[i], result[now]+time[i])
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    
    for i in range(1, N+1):
        print(result[i])

topology_sort()
     