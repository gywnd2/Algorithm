import sys
n=int(sys.stdin.readline())
words=list(sys.stdin.readline().rstrip() for _ in range(n))
words=list(set(words)); words.sort()
def quick(arr, start, end):
    if start>=end:
        return
    pivot=arr[start]; l=start; mid=start; r=end
    while mid<=r:
        if len(arr[mid])<len(pivot):
            arr[l], arr[mid]=arr[mid], arr[l]
            mid+=1
            l+=1
        elif len(arr[mid])>len(pivot):
            arr[r], arr[mid]=arr[mid], arr[r]
            r-=1
        else:
            mid+=1
    quick(arr, start, l-1)
    quick(arr, r+1, end)
quick(words, 0, len(words)-1)
lenIdx=[0]; result=[]
for i in range(len(words)-1):
    if len(words[i])!=len(words[i+1]):
        lenIdx.append(i+1)
for i in range(len(lenIdx)-1):
    res=words[lenIdx[i]:lenIdx[i+1]]
    res.sort()
    result+=res
# 나머지 뒷부분도 정렬하여 추가
if len(result)!=len(words):
    res=words[lenIdx[len(lenIdx)-1]:]
    res.sort()
    result+=res
for word in result:
    print(word)