from collections import deque
import sys

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x]=find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a=find_parent(parent, a)
    b=find_parent(parent, b)
    
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

N, M=map(int, sys.stdin.readline().strip().split())
parent=[0]*(N+1)
for i in range(1, N+1):
    parent[i]=i
for _ in range(M):
    op, a, b=map(int, sys.stdin.readline().strip().split())
    if op==0:
        union_parent(parent, a, b)
    else:
        parentA=find_parent(parent, a)
        parentB=find_parent(parent, b)
        if parentA==parentB:
            print("YES")
        else:
            print("NO")
