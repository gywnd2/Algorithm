import sys, collections
input=sys.stdin.readline()
INF=int(1e9)

def bellmanford(start):
    # 시작 노드 초기화
    dist[start]=0
    # 전체 n 번 반복
    for i in range(n):
        for j in range(m):
            # 0은 출발점, 1은 도착점, 2는 비용
            curr_node=edges[j][0]
            next_node=edges[j][1]
            cost=edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[curr_node]!=INF and dist[next_node]>dist[curr_node]+cost:
                dist[next_node]=dist[curr_node]+cost
                # n번째 반복에서도 값이 갱신된다면 음수 순환이 존재한다는 의미
                if i==n-1:
                    return True
    return False

# 노드의 개수, 간선의 개수 입력받기
n, m=map(int, input().split())
# 최단 거리 테이블을 모두 무한을 초기화
edges=[]; dist=[INF]*(n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c=map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    edges.append((a, b, c))

# 벨만포드 알고리즘 수행
negative_cycle=bellmanford(1) # 시작 노드 1번

if negative_cycle:
    print("-1")
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단거리 출력
    for i in range(2, n+1):
        # 도달할 수 없는 경우
        if dist[i]==INF:
            print("-1")
        # 도달할 수 있는 경우
        else:
            print(dist[i])