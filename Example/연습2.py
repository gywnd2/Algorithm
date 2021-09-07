from collections import deque
import sys
INF=sys.maxsize
graph=[[]]; vColor=[]

def promising(i):
    j=1; good=True
    while j<i and good:
        if graph[i][j] and vColor[i]==vColor[j]:
            good=False
        j+=1
    return good

def mColoring(i):
    if promising(i):
        if i==n:
            print(vColor)
        else:
            for color in range(2, m):
                vColor.append(color)
                mColoring(i)

def sumofsubset(i, weight, total):
    # weight+w[i+1]>W or weight+total<W 일 경우 유망하지 않음
    if weight+total>=W and (weight==W or weight+w[i+1]<=W):
        if W==weight:
            print(~~)
    else:
        sumofsubset(i+1, weight, total)

def dfs(graph, v, visited):
    visited[v]=True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

def countSortOrigin(arr, r):
    count=[0 for _ in range(r+1)]
    for digit in arr:
        count[digit]+=1
    for i in range(len(count)):
        if count[i]!=0:
            print(i*count[i],end='')
    
def countSort(arr, digit):
    temp=[0 for _ in range(len(arr))]
    cnt=[0 for _ in range(10)]
    for i in range(arr):
        cnt[(arr[i]//digit)%10]+=1
    for i in range(1, 10):
        cnt[i]=cnt[i]+cnt[i-1]
    for i in range(len(arr)-1, -1, -1):
        cntValue=(arr[i]//digit)%10
        newIdx=cnt[cntValue]-1
        temp[newIdx]=arr[i]
        cnt[cntValue]-=1
    return temp

def radixSort(arr):
    i=1
    maxVal=max(arr)
    while maxVal//i>0:
        arr=countSort(arr, i)
        i*=10
    return arr

def knapsack(limit, weight, profit, n):
    K=[[0 for _ in range(limit+1)] for _ in range(n+1)]
    for i in range(n+1):
        for w in range(limit+1):
            if i==0 or w==0:
                K[i][w]=0
            elif weight[i-1]<=w:
                K[i][w]=max(K[i-1][w-weight[i-1]]+profit[i-1], K[i-1][w])
            else:
                K[i][w]=K[i-1][w]
    return K[n][limit]

def floyd():
    nodes=int(input())
    edges=int(input())
    dist=[[INF]*(n+1) for _ in range(n+1)]

    for i in range(1, nodes+1):
        for j in range(1, nodes+1):
            if i==j:
                dist[i][j]=0
    
    for _ in range(edges):
        a, b, c=map(int, input().split())
        dist[a][b]=c

    for k in range(1, nodes+1):
        for i in range(1, nodes+1):
            for j in range(1, nodes+1):
                dist[i][j]=min(dist[i][j], dist[i][k]+dist[k][j])
    
    for i in range(1, nodes+1):
        for j in range(1, nodes+1):
            if dist[i][j]==INF:
                print("INFINITY", end='')
            else:
                print(dist[i][j], end='')
        print()

def get_smallest_node():
    min_value=INF
    index=0
    for i in range(1, n+1):
        if dist[i]<min_value and not visited[i]:
            min_value=dist[i]
            index=i
    return index

def dijkstra(start):
    dist[start]=0
    visited[start]=True
    for j in graph[start]:
        dist[j[0]]=j[1]
    for i in range(n-1):
        now=get_smallest_node()
        visited[now]=True
        for j in graph[now]:
            cost=dist[now]+j[1]
            if cost<dist[j[0]]:
                dist[j[0]]=cost

def bellmanford(start):
    dist[start]=0
    for i in range(n):
        for j in range(m):
            curr_node=edges[j][0]
            next_node=edges[j][1]
            cost=edges[j][2]
            if dist[curr_node]!=INF and dist[next_node]>dist[curr_node]+cost:
                dist[next_node]=dist[curr_node]+cost
                if i==n-1:
                    return True
    return False

negative_cycle=bellmanford(1)

if negative_cycle:
    print("-1")
else:
    for i in range(2, n+1):
        if dist[i]==INF:
            print("-1")
        else:
            print(dist[i])