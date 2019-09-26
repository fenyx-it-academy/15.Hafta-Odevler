##Cut the sticks
n = int(input())
arr = list(map(int, input().rstrip().split()))
b = [0] * 1001
for i in arr:
    b[i] += 1
counter = 0
b = b[::-1]
n =[]
for i in b:
    if i > 0:
        counter += i
        n.append(counter)
n = n[::-1]
for i in n:
    print(i)




def cutTheSticks(arr):
    b = [0] * 1001
    for i in arr:
        b[i] += 1
    counter = 0
    b = b[::-1]
    n =[]
    for i in b:
        if i > 0:
            counter += i
            n.append(counter)
    n = n[::-1]
    for i in n:
        print(i)

n = int(input())
arr = list(map(int, input().rstrip().split()))
result = cutTheSticks(arr)
print(result)
