x=int(input())
y=int(input())
xpos="+"
ypos="+"

if x<0 and x>=-1000 :
    xpos="-"
elif x>0 and x<=1000 :
    xpos="+"

if y<0 and y>=-1000 :
    ypos="-"
elif y>0 and y<=1000 :
    ypos="+"

if xpos=="+" and ypos=="+":
    print("1")
elif xpos=="+" and ypos=="-":
    print("4")
elif xpos=="-" and ypos=="+":
    print("2")
elif xpos=="-" and ypos=="-":
    print("3")