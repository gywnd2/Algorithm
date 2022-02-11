# 나중에 다시 풀자,,
string=input()
stack=list()
result=0
temp=1
for i in range(len(string)):
    if string[i]=='(':
        stack.append(string[i])
        temp*=2
    elif string[i]=='[':
        stack.append(string[i])
        temp*=3
    elif string[i]==')':
        if not stack or stack[-1]=='[':
            answer=0
            break
        elif string[-1]=='(':
            result+=
    else:
        if not stack or stack[-1]=='(':
            result=0
        
