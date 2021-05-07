h1,m1,s1=map(int, input().split(":"))
currTime=h1*3600+m1*60+s1
h2,m2,s2=map(int, input().split(":"))
endTime=h2*3600+m2*60+s2
if h1>h2:
    endTime+=86400
res=endTime-currTime
h3=res//3600
m3=(res%3600)//60
s3=((res%3600)%60)
print("%02d:%02d:%02d" %(h3, m3, s3))