N=int(input())
calls=list(map(int, input().split()))
yPlan=0; mPlan=0
for call in calls:
    if call<30:
        yPlan+=10
    else:
        quot=call//30
        yPlan+=10*quot
        if((call-quot)!=0):
            yPlan+=10

for call in calls:
    if call<60:
        mPlan+=15
    else:
        quot=call//60
        mPlan+=15*quot
        if((call-quot)!=0):
            mPlan+=15

if yPlan<mPlan:
    print("Y", yPlan)
elif yPlan>mPlan:
    print("M", mPlan)
else:
    print("Y", "M", yPlan)