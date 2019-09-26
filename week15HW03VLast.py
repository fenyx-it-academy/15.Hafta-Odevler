d1M1Y1 = input().split()

d1 = int(d1M1Y1[0])

m1 = int(d1M1Y1[1])

y1 = int(d1M1Y1[2])

d2M2Y2 = input().split()

d2 = int(d2M2Y2[0])

m2 = int(d2M2Y2[1])

y2 = int(d2M2Y2[2])
fark=[]
hd=15
hm=500
hy=10000
if (y1 - y2) < 0:
    print(0)
elif (y1 - y2) == 0 and (m1 - m2)< 0 :
    print(0)
elif (d1 - d2)< 0 and (y1 - y2) == 0  and (m1 - m2)  == 0:
    print(0)
elif (y1-y2) >= 0 or ((m1-m2))>=0 or (d1-d2)>=0:
    xy=hy* (y1-y2)
    fark.append(xy)
    xm= hm* ((m1-m2))
    fark.append(xm)
    xd= hd* (d1-d2)
    fark.append(xd)
    print(max(fark))

