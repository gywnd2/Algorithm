from collections import deque

flag=True
while True:
    string=input()
    if string==".":
        break
        
    brackets=deque()
    lBrackets=deque()
    
    for char in string:
        if char in ('(', ')', '[', ']'):
            brackets.append(char)
            
    idx=0
    while idx<len(brackets):
        if brackets[idx] in ('(', '['):
            lBrackets.append(brackets[idx])
        elif brackets[idx]==')':
            if len(lBrackets)!=0 and lBrackets[-1]=='(':
                lBrackets.pop()
            else:
                flag=False
                print('no')
                break
        elif brackets[idx]==']':
            if len(lBrackets)!=0 and lBrackets[-1]=='[':
                lBrackets.pop()
            else:
                flag=False
                print('no')
                break
        idx+=1
        
    if len(lBrackets)==0 and flag:
        print('yes')
    elif flag:
        print('no')
    flag=True