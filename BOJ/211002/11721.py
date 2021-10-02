word=list(input())
if len(word)//10==0:
    print(''.join(word))
else:
    for i in range(len(word)//10+1):
        print(''.join(word[10*i:10*(i+1)]))