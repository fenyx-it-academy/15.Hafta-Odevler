from itertools import combinations


def nonDivisibleSubset(k, s):
    s = list(set(s))
    comb = []
    subset_ok = []
    for i in range(2, len(s)):
        comb.append(list(combinations(s, i+1)))  # Finding all subset possibilities
    key = True
    while key:
        for subsets in reversed(comb):  # iterating all combinations from the biggest to smallest (reversed)
            for subset in subsets:
                if all((u + v) % k for (u, v) in combinations(subset, 2)):  # When finding a suitable subset,
                    subset_ok = subset                                      # breaking out of all loops
                    key = False
                    break
            if not key:
                break

    print(len(subset_ok))


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

s = list(map(int, input().rstrip().split()))
s.sort()

nonDivisibleSubset(k, s)