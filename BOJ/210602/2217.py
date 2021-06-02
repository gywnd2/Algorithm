# 로프 무게*index의 최대값 출력...
N=int(input())
rope=[int(input()) for _ in range(N)]
rope.sort(reverse=True)
for i in range(1, N+1):
    rope[i-1]=rope[i-1]*i
print(max(rope))