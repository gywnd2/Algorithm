import sys

n=int(sys.stdin.readline().strip())

def draw(n):
    if n==1:
        return ['*']
    
    stars=draw(n//3)
    line=[]
    
    for star in stars:
        line.append(star*3)
    for star in stars:
        line.append(star+' '*(n//3)+star)
    for star in stars:
        line.append(star*3)
    
    return line

print('\n'.join(draw(n)))