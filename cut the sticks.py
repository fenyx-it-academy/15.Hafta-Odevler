n = int(input())
arr = list(map(int, input().rstrip().split()))

print(n)
while True:
    arr = list(filter(lambda y: y > 0, map(lambda x: x - min(arr), arr)))
    if len(arr) == 0:
        break
    print(len(arr))
