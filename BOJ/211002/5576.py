score=list(int(input()) for _ in range(20))
a=score[:10]
a.sort(reverse=True)
b=score[10:]
b.sort(reverse=True)
print(sum(a[:3]), sum(b[:3]))