def solution(s):
    answer = ''
    s=list(map(str, s))
    for i in range(len(s)):
        s[i]=ord(s[i])
    s.sort(reverse=True)
    for i in range(len(s)):
        s[i]=chr(s[i])
        answer+=s[i]
    return answer
print(solution("Zbcdefg"))