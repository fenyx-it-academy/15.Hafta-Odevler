n = int(input())
arr = list(map(int, input().rstrip().split()))
print(len(arr))
while True:
    arr = [x for x in arr if x != min(arr)]
    if len(arr)==0:
        break
    print(len(arr))