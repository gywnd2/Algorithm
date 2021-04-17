import sys
while True:
    t = int(sys.stdin.readline())
    if t==0:
        break
    dic = list(sys.stdin.readline().strip() for _ in range(t))
    originDic = dic.copy()
    lowerDic = []
    for word in dic:
        lowerDic.append(word.lower())
    for i in range(len(dic)):
        dic[i] = dic[i].lower()
    lowerDic.sort()
    print(originDic[dic.index(lowerDic[0])])