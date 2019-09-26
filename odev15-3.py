##  Library Fine


def libraryFine(d1, m1, y1, d2, m2, y2):
    ceza=0
    if y1 < y2 or (m1 < m2 and y1 == y2) or (d1 <= d2 and m1 == m2 and y1 == y2):
        ceza=0
    elif d1 > d2 and m1 == m2 and y1 == y2:
        ceza+=15*(d1-d2)
    elif m1 > m2 and y1 == y2:
        ceza+=500*(m1-m2)
    else:
        ceza+=10000
    return ceza
        
d1M1Y1 = input().split()
d1 = int(d1M1Y1[0])
m1 = int(d1M1Y1[1])
y1 = int(d1M1Y1[2])
d2M2Y2 = input().split()
d2 = int(d2M2Y2[0])
m2 = int(d2M2Y2[1])
y2 = int(d2M2Y2[2])
result = libraryFine(d1, m1, y1, d2, m2, y2)
print(result)
