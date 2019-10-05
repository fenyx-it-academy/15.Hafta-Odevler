


def libraryFine(d1, m1, y1, d2, m2, y2):
    
    if y1<=y2:
        if y1<y2:
            return 0
        else:
            if m1<m2:
                return 0
            if m1==m2:
                if d1<=d2:
                    return 0
    
    if y1==y2:
        if m1= =m2:
            return (d1-d2)*15
        else:
            return (m1-m2)*500
    else:
        return (y1-y2)*10000

print(libraryFine(12,8,2018,4,5,2017))




