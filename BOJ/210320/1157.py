word=input()
countWord={}
for spell in word:
    if 65<=ord(spell)<=90:
        try:
            countWord[spell]+=1
        except:
            countWord[spell]=1
    else:
        try:
            countWord[chr(ord(spell)-32)] += 1
        except:
            countWord[chr(ord(spell)-32)] = 1

valueList=list(countWord.values())
maxValue=max(valueList)
if valueList.count(maxValue)>1:
    print("?")
else:
    print(max(countWord, key=countWord.get))