#인덱스 상으로 뒤에 있는 글자가 find로 인덱스 값을 찾았을 때
#실제 인덱스 순서를 거스르는 결과가 나온다면 그룹단어가 아니다.

n=int(input())
count=n
for _ in range(n):
    word=input()
    for i in range(len(word)-1):
        if word.find(word[i])>word.find(word[i+1]):
            count-=1
            break
print(count)