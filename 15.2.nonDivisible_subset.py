print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

from collections import Counter


def nonDivisiblesubsetset(k, s):
    count = 0                                                   # eleman sayisi enfazla altkume sayi counter
    subset = Counter(map(lambda x: (x % k), s))                 # k sayisina bolunmeyen ciftlerin alt kumelerini buluyor
    for i in range(1, (k // 2) + 1):
        j = k - i
        if (i == j) and (subset[i] > 0):
            count += 1
        elif subset[i] > subset[j]:
            count += subset[i]
        else:
            count += subset[j]
    if subset[0] > 0:
        count += 1
    return print(count)


first_multiple_input = input().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
s = list(map(int, input().split()))
nonDivisiblesubsetset(k, s)
