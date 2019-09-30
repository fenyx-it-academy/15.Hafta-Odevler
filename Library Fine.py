def libraryFine(d1, m1, y1, d2, m2, y2):
    fine = 0
    if y2 > y1:
        return 0
    if y1 == y2 and m1 == m2 and d1 < d2:
        return 0
    if y1 == y2 and m1 == m2 and d1 == d2:
        return 0
    if y1 == y2 and m2 > m1:
        return 0
    if y1 > y2 and m1 == m2 and d1 == d2:
        return (y1 - y2) * 10000
    if y1 != y2 and m1 != m2 and d1 != d2:
        fine += (y1 - y2) * 10000
    elif y1 != y2 and m1 == m2 and d1 != d2:
        fine += (y1 - y2) * 10000
    elif y1 == y2 and m1 != m2 and d1 != d2:
        fine += (m1 - m2) * 500
    elif y1 == y2 and m1 == m2 and d1 != d2:
        fine += (d1 - d2) * 15
    return (fine)





libraryFine(29,7,2015,6,6,2015)