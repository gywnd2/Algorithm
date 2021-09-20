# String으로 풀면 list로 변환 했을 때 두 자리 숫자가 하나하나 쪼개짐
# a, b=map(int, input().split())
# series=""; result=0; num=1
# while len(series)<b:
#     if num==1:
#         series+="1"
#     else:
#         series+=(str(num)*num)
#     num+=1
# series=list(series)
# print(series)
# series=series[a-1:b]
# print(series)
# for i in series:
#     result+=int(i)
# print(result)

#  series+=[i]*i
a, b=map(int, input().split())
series=[]
for i in range(b+1):
    series+=[i]*i
series=series[a-1:b]
print(sum(series))