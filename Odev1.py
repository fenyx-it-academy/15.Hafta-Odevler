def cutTheSticks(arr,n):
    liste = []
    finish = False

    while finish == False:
        minElement = 10000000000
        count = 0
        finish = True
        for i in arr:
            if i < minElement and i != 0:
                minElement = i

        if len(liste) == 0:
            liste.append(str(n))

        arr = list(map(lambda x: x - minElement if(x > minElement)else 0, arr))
        if sum(arr) != 0:
            finish = False
        for i in arr:
            if i == 0:
                count += 1
        if n - count != 0:
            liste.append(str(n - count))
        else:
            break
    liste = '\n'.join(liste)
    return print(liste)

n = int(input())

arr = list(map(int, input().rstrip().split()))

result = cutTheSticks(arr, n)

