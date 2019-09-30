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