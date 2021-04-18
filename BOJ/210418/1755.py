import sys
m, n=map(int, sys.stdin.readline().strip().split())
num=list(i for i in range(m, n+1))
dic=[]
for i in range(len(num)):
    temp=str(num[i])
    word=''
    for j in range(len(temp)):
        if temp[j]=='0':
            word+="zero"
            word+=' '
        elif temp[j]=='1':
            word+="one"
            word+=' '
        elif temp[j]=='2':
            word+="two"
            word+=' '
        elif temp[j]=='3':
            word+="three"
            word+=' '
        elif temp[j]=='4':
            word+="four"
            word+=' '
        elif temp[j]=='5':
            word+="five"
            word+=' '
        elif temp[j]=='6':
            word+="six"
            word+=' '
        elif temp[j]=='7':
            word+="seven"
            word+=' '
        elif temp[j]=='8':
            word+="eight"
            word+=' '
        else:
            word+="nine"
            word+=' '
    dic.append(word)
dic.sort()
num.clear()
for word in dic:
    word=word.split()
    wordStr=''
    for i in range(len(word)):
        if word[i]=="zero":
            wordStr+='0'
        elif word[i]=="one":
            wordStr+='1'
        elif word[i]=="two":
            wordStr+='2'
        elif word[i]=="three":
            wordStr+='3'
        elif word[i]=="four":
            wordStr+='4'
        elif word[i]=="five":
            wordStr+='5'
        elif word[i]=="six":
            wordStr+='6'
        elif word[i]=="seven":
            wordStr+='7'
        elif word[i]=="eight":
            wordStr+='8'
        else:
            wordStr+='9'
    num.append(int(wordStr))
for n in range(len(num)):
    if n%10==0 and n!=0:
        print()
    print(num[n],"", end='')