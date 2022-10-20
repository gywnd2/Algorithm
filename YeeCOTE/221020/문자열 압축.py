import sys
def solution(s):
    answer = []
    block=8
    while block<=len(s)//2:
        res=''
        tmp=[s[i:i+block] for i in range(0, len(s), block)]
        idx=0; count=1; start=0
        while idx<=len(tmp)-2:
            if idx==len(tmp)-2: 
                if count!=1:
                    if tmp[idx]==tmp[-1]:
                        count+=1
                    res+=str(count)
                    res+=tmp[idx]
                else:
                    if tmp[idx]==tmp[idx+1]:
                        count+=1
                        res+=str(count)
                        for i in tmp[idx:idx+count]:
                            res+=i
                    else:
                        for i in tmp[idx:]:
                            res+=i
            else:
                if tmp[idx]==tmp[idx+1]:
                    count+=1
                else:
                    if count==1:
                        res+=tmp[idx]
                    else:
                        res+=str(count)
                        res+=tmp[start]
                        start=start+count
                        count=1
            idx+=1
        block+=1
        answer.append(len(res))
        print(block, len(res), res)
        res=''
    return min(answer)

print(solution('ababcdcdababcdcd'))