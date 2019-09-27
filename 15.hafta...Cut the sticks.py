def cutTheSticks():
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    while len(arr) != 0:
        print(len(arr))
        for i in range(arr.count(min(arr))):
            arr.remove(min(arr))
cutTheSticks()