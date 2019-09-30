def libraryFine():
    d1M1Y1 = list(map(int, input().split()))

    d1 = d1M1Y1[0]

    m1 = d1M1Y1[1]

    y1 = d1M1Y1[2]

    d2M2Y2 = list(map(int, input().split()))

    d2 = d2M2Y2[0]

    m2 = d2M2Y2[1]

    y2 = d2M2Y2[2]

    if y1 < y2:
        print(0)
    elif y1==y2:
        if m1 < m2:
            print(0)
        elif m1 == m2:
            if d1 <= d2:
                print(0)
            else:
                print((d1-d2)*15)
        else:
            print((m1-m2)*500)
    else:
        print(10000)

libraryFine()

    # result = libraryFine(d1, m1, y1, d2, m2, y2)
    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()