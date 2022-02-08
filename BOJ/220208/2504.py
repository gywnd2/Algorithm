string=input()
stack=list()
result=1
for i in range(len(string)):
    if string[i] in ('(', '['):
        stack.append(string[i])
    else:
        if string[i]==')' and stack[-1]=='(':
            if string[i-1] in (2, 3):
                while string[i-1] not in (2, 3):
                    result*=string[i-1]
                    stack.pop()
                result*=2
                stack.pop()
            else:
                stack.pop()
                stack.append(2)
        elif string[i]==']' and stack[-1]=='[':
            if string[i-1] in (2, 3):
                while string[i-1] not in (2, 3):
                    result*=string[i-1]
                    stack.pop()
                result*=3
                stack.pop()
            else:
                stack.pop()
                stack.append(3)
if len(stack)==0:
    print(result)
else:
    print(0)
