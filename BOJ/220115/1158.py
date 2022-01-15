from collections import deque

n, k = map(int, input().split())
circle = deque(i for i in range(1, n+1))

result = list()
tmp = list()
index = 0
while len(circle) != 0:
    index += k-1
    if index >= len(circle):
        index %= len(circle)
    result.append(circle[index])
    circle.remove(circle[index])
print("<", ', '.join(str(i) for i in result), ">", sep = '')