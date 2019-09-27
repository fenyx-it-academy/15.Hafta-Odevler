def nonDivisibleSubset():
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = list(map(int, input().rstrip().split()))
    a = []
    for i in s:
        for j in s:
            if i != j and (i + j) % k != 0:
                t = [i, j]
                t.sort()
                if t not in a:
                    a.append(t)
    b = []
    for i in a:
        for j in i:
            if j not in b:
                b.append(j)
    for i in b:
        for j in b:
            if i != j and (i + j) % k == 0:
                b.remove(j)

    print(len(b))
nonDivisibleSubset()
