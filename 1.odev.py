def cutTheSticks():

    n = int(input())
    arr = input().split()
    print(len(arr))  # arrin ilk islem gerceklesmeden halin = int(input())

    for i in range(n):
        arr[i] = int(arr[i])
    while len(arr) != 0:
        m = min(arr)
        for i in range(len(arr)):
            arr[i] = arr[i]-m

        for l in range(arr.count(0)):
            arr.remove(0)

        if len(arr) == 0:
            break

        print(len(arr))


cutTheSticks()


