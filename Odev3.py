# alis: 5.9.2018
# iade: 6.12.2018
def libraryFine(d1, m1, y1, d2, m2, y2):
    if (d1 == d2 and y1 == y2 and m1 == m2) or y1 < y2 or (d1 < d2 and m1 <= m2 and y1 <= y2) or (m1 < m2 and y1 <= y2):
        return print(0)
    elif(m1 == m2 and y1 == y2 and d1 > d2):
        return print((d1-d2)*15)
    elif(m1 > m2 and y1 == y2):
        return print((m1 - m2)*500)
    elif(y1 > y2):
        return print(10000)
    else:
        print('err')


d1M1Y1 = input().split()

d1 = int(d1M1Y1[0])

m1 = int(d1M1Y1[1])

y1 = int(d1M1Y1[2])

d2M2Y2 = input().split()

d2 = int(d2M2Y2[0])

m2 = int(d2M2Y2[1])

y2 = int(d2M2Y2[2])

result = libraryFine(d1, m1, y1, d2, m2, y2)

