n=int(input())
for _ in range(n):
    string=list(input())
    string[0]=string[0].upper()
    print(''.join(string))