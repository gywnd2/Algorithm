from collections import deque
import sys
INF=sys.maxsize
graph=[[]]; vColor=[]

def promising(i):
    j=1; good=True
    while j<i and good:
        # 연결되어 있고 색이 같은지
        if graph[i][j] and vColor[i]==vColor[j]:
            good=False
        j+=1
    return good

# 1부터 시작
def mColoring(i):
    if promising(i):
        if i==n:
            # 1부터 N까지 출력
            print(vColor)
        else:
            # 1은 이미 했으므로 2 부터 모든 정점의 색 확인
            for color in range(2, m):
                vColor.append(color)
                mColoring(i)

def sumofsubset(i, weight, total):
    # 가지치기 조건 기억하기
    # weight+w[i+1]>W or weight+total<W 일 경우 유망하지 않음
    if weight+total>=W and (weight==W or weight+w[i+1]<=W):
        if W==weight:
            print
    else: 
        sumofsubset(i+1,weight, total)

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
    # 각 원소의 끝 숫자 하나씩 추출해서 카운트
    for i in range(len(arr)):
        cnt[(arr[i]//digit)%10]+=1
    # 개수 누적하기
    for i in range(1, 10):
        cnt[i]=cnt[i]+cnt[i-1]
    # arr의 역순으로
    for i in range(len(arr)-1, -1, -1):
        # ex) 251 이고 digit=1 : (251//1)%10=1
        #              digit=10 : (251//10)%10=5
        cntValue=(arr[i]//digit)%10
        # cnt값-1 = 반복의 끝자리 인덱스
        newIdx=cnt[cntValue]-1
        # 구한 인덱스대로 정렬의 결과인 temp에 새로 대입
        temp[newIdx]=arr[i]
        # 하나 대입했으니 cnt 하나 감소
        cnt[cntValue]-=1
    #temp는 지역변수 이므로 return하지 않으면 소멸됨
    return temp

def radixSort(arr):
    i=1
    # 정렬할 배열의 최대값 찾기
    maxVal=max(arr)
    # 최대값의 최대 기수까지 진행
    while maxVal//i>0:
        arr=countSort(arr, i)
        i*=10
    return arr


weight=[6, 4, 3, 6]; profit=[13, 8, 6, 12]

def knapsack(limit, weight, profit, n):
    K=[[0 for _ in range(limit+1)] for _ in range(n+1)]
    for i in range(n+1):
        for w in range(limit+1):
            # 0행, 0열은 모두 0으로 초기화
            if i==0 or w==0:
                K[i][w]=0
            # 넣을 때
            elif weight[i-1]<=w:
                # 그렇지 않다면 i번째 물건을 위해 무게를 비웠을 때의 최적값에
                # i번째 보석의 가격을 더한 값 or
                #  전 단계의 최적 값 중 가장 큰 것을 선택
                K[i][w]=max(K[i-1][w-weight[i-1]]+profit[i-1], K[i-1][w])
            # 넣지 않았을 때
            else:
                # i번째 물건이 한도 초과를 발생시킨다면 버림
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
                print("INFINITY", end=' ')
            else:
                print(dist[i][j], end=' ')
        print()

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