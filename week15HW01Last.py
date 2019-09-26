n = int(input())
arr = list(map(int, input().rstrip().split()))
arr.sort(reverse=True)
while len(arr) > 0:
    print(len(arr))
    k = min(arr)
    while len(arr) > 0 and arr[-1] <= k:
        shortt = arr.remove(k)
