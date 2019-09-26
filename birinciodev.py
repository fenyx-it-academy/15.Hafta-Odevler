list = []
def pageCount(n, p):
    i = 0
    while i < n + 1:
        if i == n:
            list.append([i, 0])
        else:
            list.append([i, i + 1])
        i +=2
    for i in list:
        for j in i:
            if j == n:
                indexN = list.index(i)
            if j == p:
                indexP = list.index(i)
    fromFirst = indexP
    fromLast = indexN - indexP
    if fromFirst < fromLast:
        return print(fromFirst)
    else:
        return print (fromLast)

n = int(input())

p = int(input())

pageCount(n, p)
































