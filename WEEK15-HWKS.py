###ODEV1

# arr = input('ent the list').split() #to make a list from space seperated integers in string type

"""
Aim: for each iteration, print the number of sticks left
"""




def cutTheSticks(): #put tghe list as an arg ####ICINE ARGUMANLA NEDEN CAGRILMIYOR

    n = int(input())
    arr = input().split()
    print(len(arr))  # arrin ilk islem gerceklesmeden halin = int(input())

    for i in range(n):
        arr[i] = int(arr[i])
    while len(arr) != 0:
        m = min(arr)
        for i in range(len(arr)):
            arr[i] = arr[i]-m

        for l in range(arr.count(0)):
            arr.remove(0)

        if len(arr) == 0:
            break

        print(len(arr))


cutTheSticks()

###ODEV2

def libraryFine():
    d1M1Y1 = list(map(int, input().split()))

    d1 = d1M1Y1[0]

    m1 = d1M1Y1[1]

    y1 = d1M1Y1[2]

    d2M2Y2 = list(map(int, input().split()))

    d2 = d2M2Y2[0]

    m2 = d2M2Y2[1]

    y2 = d2M2Y2[2]

    if y1 < y2:
        print(0)
    elif y1==y2:
        if m1 < m2:
            print(0)
        elif m1 == m2:
            if d1 <= d2:
                print(0)
            else:
                print((d1-d2)*15)
        else:
            print((m1-m2)*500)
    else:
        print(10000)

libraryFine()

    # result = libraryFine(d1, m1, y1, d2, m2, y2)
    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()



#########ODEV3   ######BU YAPMAYA CALISTIGIM
# S: an array of integers
#k: an integer
n_k = input().split()  # enter 2 space seperated integers: n and k
S = input().split()  # n number of unique values (for our set), now it is a list, we should make it set somehere

n = int(n_k[0])
k = int(n_k[1])

for i in range(n):
    S[i] = int(S[i])
subsets = []
def nonDivisibleSubset(S, k):
    for i in S:
        for j in S:
            if (i +S[j]) % k != 0:
                subsets.append([i]) #her iterationdan ayri ikililer gelecek, ama birbirinin ayni olan i
                subsets.append([j])  #veya jler de gelebilir. bu yuzden ikili degil tekli append yapip
                                        #sonra da set()'e donusturmeliyiz.
            return len(set(subsets))

nonDivisibleSubset(S, k)

#################Internetten aldigim ama bu da hackerranktenkin oz saglamiyor

def subsetPairNotDivisibleByK(arr, N, K):
    # Array for storing frequency
    # of modulo values
    f = [0 for i in range(K)]

    # Fill frequency array with
    # values modulo K
    for i in range(N):
        f[arr[i] % K] += 1

    # if K is even, then update f[K/2]
    if (K % 2 == 0):
        f[K / 2] = min(f[K / 2], 1)

        # Initialize result by minimum of 1 or
    # count of numbers giving remainder 0
    res = min(f[0], 1)

    # Choose maximum of count of numbers
    # giving remainder i or K-i
    for i in range(1, (K // 2) + 1):
        res += max(f[i], f[K - i])

    return res


# Driver Code
arr = [3, 7, 2, 9, 1]
N = len(arr)
K = 3
print(subsetPairNotDivisibleByK(arr, N, K))




    
