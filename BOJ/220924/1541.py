expr=input()
expr=expr.split('-')
res=''
idx=0
# print(expr)
while idx<len(expr):
    if idx!=0:
        tmp=expr[idx].split('+')
        res+='-'
        res+='('
        i=0
        while i<len(tmp):
            res+=str(int(tmp[i]))
            if i!=len(tmp)-1:
                res+='+'
            i+=1
        if idx!=0:
            res+=')'
        idx+=1
    else:
        tmp=expr[idx].split('+')
        i=0
        while i<len(tmp):
            res+=str(int(tmp[i]))
            if i!=len(tmp)-1:
                res+='+'
            i+=1
        idx+=1
# print(res)
print(eval(res))