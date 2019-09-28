def cutTheSticks(arr):
    while arr:
        print(len(arr))
        for i in range(arr.count(min(arr))):
            arr.remove(min(arr))

n = int(input())
arr = list(map(int, input().rstrip().split()))
cutTheSticks(arr)