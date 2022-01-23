t=int(input())

flag=True
for _ in range(t):
    string=list(input())
    stack=list()
    for bracket in string:
        if bracket=='(':
            stack.append(bracket)
        elif bracket==')' and len(stack)!=0 and stack[-1]=='(':
            stack.pop()
        else:
            flag=False
            print('NO')
            break
    if len(stack)==0 and flag:
        print('YES')
    elif len(stack)!=0 and flag:
        print('NO')
    stack.clear()
    flag=True