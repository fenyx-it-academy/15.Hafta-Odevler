def cutTheSticks(arr):
    for i in range(len(arr)):
        while len(arr) != 0:
            length = len(arr)
            shortest = min(arr)
            while shortest in arr: arr.remove(shortest)
            for j in range(len(arr)):
                arr[j] -= shortest

            print(length)
    return arr


n = int(input())

arr = list(map(int, input().rstrip().split()))

cutTheSticks(arr)
