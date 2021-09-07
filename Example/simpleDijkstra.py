import sys
input= sys.stdin.readline
INF=int(1e9)

# 노드 , 간선 개수 입력 받기
n,m=map(int, input().split())
# 시작 노드 번호 입력
start=int(input())
# 그래프 초기화
graph=[[] for i in range(n+1)]
# 방문 여부 초기화
visited=[False]*(n+1)
# 최단 거리 테이블 초기화
dist=[INF]*(n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c=map(int, input().split())
    # a -> b의 비용이 c
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서 가장 최단거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value=INF
    # 가장 최단거리가 짧은 노드의 인덱스
    index=0
    for i in range(1, n+1):
        if dist[i] < min_value and not visited[i]:
            min_value=dist[i]
            index=i
    return index

def dijkstra(start):
    # 시작 노드 초기화
    dist[start]=0
    visited[start]=True
    for j in graph[start]:
        # 0은 도착점, 1은 비용
        dist[j[0]]=j[1]
    # 시작 노드를 제외한 전체 n-1개 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
        now=get_smallest_node()
        visited[now]=True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            # 비용= 현재 점까지의 비용 + 도착점 까지의 비용
            cost=dist[now]+j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost<dist[j[0]]:
                dist[j[0]]=cost
# 다익스트라 수행
dijkstra(start)
# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우 무한 으로 출력
    if dist[i]==INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리 출력
    else:
        print(dist[i])