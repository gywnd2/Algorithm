from collections import deque
import sys

"""
F : 전체 층수
S : 현재 층
G : 목적 층
U : 상승 버튼
D : 하강 버튼
"""
f,s,g,u,d=map(int, sys.stdin.readline().strip().split())

ds=[u, -d]

def bfs():
    while q:
        s=q.popleft()
        if s==g:
            print(visited[s])
            return
        for i in range(2):
            ns=s+ds[i]
            if 0<ns<=f and ns not in visited:
                q.append(ns)
                visited[ns]=visited[s]+1
        
        """ -> s==g 일 경우 바로 정답을 출력하면 되지만 아래 처럼하면 뱅뱅 돌아서 큰값을 출력하게 됨
        for i in range(2):
            ns=s+ds[i]
            if ns==g: -> 범위 확인이 빠져서 안됨!! ex) 0 이하거나 f 초과
                print(visited[s]+1)
                return
            if 0<ns<=f and ns not in visited:
                q.append(ns)
                visited[ns]=visited[s]+1
        """
        
    if visited.get(g)==None:
        print('use the stairs')
    
q=deque()
visited={}
q.append(s)
visited[s]=0
bfs()