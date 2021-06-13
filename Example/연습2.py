from collections import deque
import sys
INF=sys.maxsize
vColor=[]

def promising(i):
    j=1; good=True
    while j<i and good:
        if W[i][j] and vColor[i]==vColor[j]:
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
        print(v, end=' ')
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
            for _ in range(count[i]):
                print(i, end=' ')

def countSort(arr, digit):
    temp=[0 for _ in range(len(arr))]
    cnt=[0 for _ in range(10)]
    for i in range(len(arr)):
        # 맨 끝자리 숫자 구하기
        cnt[(arr[i]//digit)%10]+=1
    for i in range(1, 10):
        # cnt 누적하기
        cnt[i]=cnt[i]+cnt[i-1]
    for i in range(len(arr)-1, -1, -1):
        # 맨 끝자리 숫자 구하기
        cntValue=(arr[i]//digit)%10
        # cnt 인덱스 하나 감소한 다음
        newIdx=cnt[cntValue]-1
        # temp의 해당 인덱스에 해당 숫자 대입
        temp[newIdx]=arr[i]
        # cntValue에서 1 감소
        cnt[cntValue]-=1
    return temp

def radixSort(arr):
    i=1
    maxVal=max(arr)
    while maxVal//i>0:
        arr=countSort(arr, i)
        i*=10
    return arr

weight=[6, 4, 3, 6]; profit=[13, 8, 6, 12]; W=[[]]
N=4; K=7

def knapsack(W, weight, profit, n):
    K=[[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w]=0
            elif weight[i-1]<=w:
                K[i][w]=max(K[i-1][w-weight[i-1]]+profit[i-1], K[i-1][w])
            else:
                K[i][w]=K[i-1][w]
    return K[n][W]

a=[[0, 2, INF, 4], [2, 0, INF, 5], [3, INF, 0, INF], [INF, 2, 1, 0]]

def floyd():
    dist=[[INF]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            dist[i][j]=a[i][j]
    for k in range(4):
        for i in range(4):
            for j in range(4):
                if dist[i][j]>dist[i][k]+dist[k][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]
    return dist

arr=[
    1,3,2,4,3,2,5,3,1,2,
    3,4,2,4,5,2,1,3,5,2,
    1,2,2,4,4,2,3,1,2,5
]

# 각 노드와 그 인접한 노드를 작은 순으로 입력
graph=[
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 모든 노드의 방문여부는 False에서 시작
visited=[False]*9 

dist = floyd()
#arr=radixSort(arr)