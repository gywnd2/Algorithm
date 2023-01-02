import heapq, sys
input=sys.stdin.readline

N, M, C=map(int, input().split())
graph=[[] for _ in range(N+1)]
distance=[int(1e9) for _ in range(N+1)]
city=[]; res=0; maxCost=0
for _ in range(M):
    a, b, c=map(int, input().split())
    graph[a].append((b, c))

def dijikstra(start):
    global maxCost
    q=[]
    distance[start]=0
    heapq.heappush(q, (0, start))
    while q:
        dist, now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            if i[1] not in city :
                city.append(i[1])
            cost=distance[now]+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                maxCost=max(maxCost, cost)
                heapq.heappush(q, (cost, i[0]))

dijikstra(C)

print(len(city), maxCost)
