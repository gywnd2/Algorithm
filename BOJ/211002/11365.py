code=[]
while True:
    inputCode=input()
    if inputCode!="END":
        inputCode=list(inputCode)
        inputCode.reverse()
        inputCode=''.join(inputCode)
        code.append(inputCode)
    else:
        for sentence in code:
            print(sentence)
        break