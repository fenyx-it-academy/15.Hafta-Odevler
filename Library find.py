d1,m1,y1=1 ,1 ,2015
d2,m2,y2=31, 12 ,2014
dt1=d1+m1*30+y1*365
dt2=d2+m2*30+y2*365
# print(dt1)
# print(dt2)
if (dt1-dt2)>364or y1>y2:
    print(10000)
elif (dt1-dt2)>30:
    print((m1-m2)*500)
elif y2==y1 and m1==m2 and d1>d2:

    print((d1-d2)*15)

else:
    print(0)
