print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:                                                     # yil gecmis ise
        return print(10000)
    elif y2 == y1 and m1 > m2:                                      # yil ayni ama ay gecmis ise
        return print(500 * (m1 - m2))
    elif y2 == y1 and m2 == m1 and d1 > d2:                         # yil ve ay ayni gun gecmis ise
        return print(15 * (d1 - d2))
    else:
        return print(0)


d1M1Y1 = input().split()
d1 = int(d1M1Y1[0])
m1 = int(d1M1Y1[1])
y1 = int(d1M1Y1[2])
d2M2Y2 = input().split()
d2 = int(d2M2Y2[0])
m2 = int(d2M2Y2[1])
y2 = int(d2M2Y2[2])

libraryFine(d1, m1, y1, d2, m2, y2)
