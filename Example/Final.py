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
    # 노드를 방문처리하고 출력
    visited[v]=True
    print(v, end='')
    # 각 노드와 인접한 노드를 전부 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i , visited)

def bfs(graph, start, visited):
    # deque 라이브러리를 이용해 큐 생성
    queue=deque([start])
    # 시작 노드 방문처리
    visited[start]=True
    # 큐가 다 비워질 때 까지 수행
    while queue:
        # 큐에서 하나 뽑아 출력
        v=queue.popleft()
        print(v, end='')
        # 방문 했던 노드가 아니라면
        # 인접한 노드를 모두 큐에 삽입하고
        # 방문 노드를 방문 처리
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
                print(i, end='')

def countSort(arr, digit):
    temp=[0 for _ in range(len(arr))]
    cnt=[0 for _ in range(10)]
    for i in range(len(arr)):
        cnt[(arr[i]//digit)%10]+=1
    for i in range(1, 10):
        cnt[i]=cnt[i]+cnt[i-1]
    for i in range(len(arr)-1, -1, -1):
        # ex) 251 이고 digit=1 : (251//1)%10=1
        #              digit=10 : (251//10)%10=5
        cntValue=(arr[i]//digit)%10
        newIdx=cnt[cntValue]-1
        temp[newIdx]=arr[i]
        cnt[cntValue]-=1
    #temp는 지역변수 이므로 return하지 않으면 소멸됨
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
def dpKnapsack(W, weight, profit, n):
    K=[[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            # 0행, 0열은 모두 0으로 초기화
            if i==0 or w==0:
                K[i][w]=0
            # 넣을 때
            elif weight[i-1]<=w:
                K[i][w]=max(K[i-1][w-weight[i-1]]+profit[i-1], K[i-1][w])
            # 넣지 않았을 때
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