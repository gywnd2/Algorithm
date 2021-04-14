dialName=input()
time=0
for n in dialName:
    if n==1:
        time+=2
    elif 65<=ord(n)<=67:
        time+=3
    elif 68<=ord(n)<=70:
        time+=4
    elif 71<=ord(n)<=73:
        time+=5
    elif 74<=ord(n)<=76:
        time+=6
    elif 77<=ord(n)<=79:
        time+=7
    elif 80<=ord(n)<=83:
        time+=8
    elif 84<=ord(n)<=86:
        time+=9
    elif 87<=ord(n)<=90:
        time+=10
    elif n==0:
        time+=11
print(time)