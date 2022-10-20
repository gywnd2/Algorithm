import sys, heapq
n, m, c=map(int, sys.stdin.readline().strip().split())
graph=[[] for _ in range(n+1)]
distance=[sys.maxsize for _ in range(n+1)]
maxCost=0; count=0
for _ in range(m):
    start, dest, cost=map(int, sys.stdin.readline().strip().split())
    graph[start].append((dest, cost))
    
def dijikstra(start):
    global count, maxCost
    q=[]
    heapq.heappush(q, (0, start))
    distance[start]=0
    while q:
        dist, now=heapq.heappop(q)
        count+=1
        maxCost=max(maxCost, dist)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q, (cost, i[0]))

dijikstra(start)
print(count-1, maxCost)