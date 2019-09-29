def nonDivisibleSubset(k, s):
    arr = []
    arr2 = []
    for i in s:
        for j in s:
            if i != j:
                if(i+j) % k != 0:
                    print('{} + {} = {} % 4 = {}'.format(i,j,i+j,(i+j)%k))
                    if i not in arr:
                        arr.append(i)
                    if j not in arr:
                        arr.append(j)
                else:
                    if j not in arr and i in arr:
                        arr2.append(j)
                    else:
                        arr2.append(i)


    print(arr)

    return print(len(arr))


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

s = list(map(int, input().rstrip().split()))

result = nonDivisibleSubset(k, s)

# to be continued