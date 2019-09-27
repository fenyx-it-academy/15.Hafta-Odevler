def libraryFine(d1, m1, y1, d2, m2, y2):
    borc = 10.000
    if d1<1 or d1>31 or 1>d2 or d2>31:
        print('day 1-31')
    if m1<1 or m1>12 or m2<1 or m1>12:
        print('mont1-12')
    if y1<1 or y1>3000 or y2<1 or y2>3000:
        print('year 1-3000')
    if  y1>y2:
        pass
    else:
        if m1!=m2:
            x=(m1-m2)*500
            borc=x
        else:
            x=(d1-d2)*15
            borc=x
    print(borc)
d1M1Y1 = input().split()
d1 = int(d1M1Y1[0])
m1 = int(d1M1Y1[1])
y1 = int(d1M1Y1[2])
d2M2Y2 = input().split()
d2 = int(d2M2Y2[0])
m2 = int(d2M2Y2[1])
y2 = int(d2M2Y2[2])
result = libraryFine(d1, m1, y1, d2, m2, y2)
