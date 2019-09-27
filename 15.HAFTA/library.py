d1m1y1 = list(input("please Enter starting date: "))
d2m2y2 = list(input("Enter return date: "))
if d1m1y1[0] == d2m2y2[0] and d1m1y1[1] == d2m2y2[1] and d1m1y1[2] == d2m2y2[2]:
    print(0)
if d2m2y2[0]>d1m1y1[0] and d1m1y1[1] == d2m2y2[1] and d1m1y1[2] == d2m2y2[2]:
    print(15*(d2m2y2[0]-d1m1y1[0]))
if d2m2y2[1]>d1m1y1[1] and d1m1y1[2]==d2m2y2[2]:
    print(500*(d2m2y2[1]-d1m1y1[1]))

if d2m2y2[2]>d1m1y1[2]:
    print(10000)


