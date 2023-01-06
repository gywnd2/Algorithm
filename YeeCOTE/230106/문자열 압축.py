from collections import deque
def solution(s):
    if len(s)==1:
        return 1
    answer = 0
    res=[]
    for i in range(1,len(s)//2+1):
        tmp=''
        q=[s[:i]]
        for j in range(0, len(s), i):
            if s[j+i:j+2*i]==s[j:j+i]:
                q.append(s[j+i:j+2*i])
            else:
                if len(q)==1:
                    tmp+=q[0]
                else:
                    tmp+=str(len(q))
                    tmp+=q[0]
                if s[j+i:j+2*i]!='':
                    q=[s[j+i:j+2*i]]
                    
        print(tmp)
        res.append(len(tmp))
    answer=min(res)
    return answer

solution('aabbaccc')