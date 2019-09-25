def cutTheSticks():
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    print(len(arr))
    while len(arr)!=0:
        minimum=min(arr)
        arr=list(filter(lambda i: i!=0, map(lambda i: i-minimum,arr)))
        if len(arr)!=0:
            print(len(arr))

result = cutTheSticks()

# 6
# 5 4 4 2 2 8