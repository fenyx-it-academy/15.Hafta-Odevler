from itertools import combinations

def nonDivisibleSubset_(k, arr):
    nonDivisibles = []
    for i in range(2, len(arr) + 1):
        combination = combinations(arr, i)
        for comb in combination:
            sub_combs = combinations(list(comb), 2)
            for sub_comb in sub_combs:
                sub_comb_sum = sum(list(sub_comb))
                if sub_comb_sum % k != 0:
                    sorted_sub_comb = sorted(list(sub_comb))
                    if sorted_sub_comb not in nonDivisibles:
                        print(list(comb), sorted_sub_comb)
                        nonDivisibles.append(sorted_sub_comb)
    return len(nonDivisibles)

def nonDivisibleSubset__(k, arr):
    arr.sort()
    nonDivisibles = []
    combination = combinations(arr, 2)
    for comb in combination:
        comb_sum = sum(list(comb))
        if comb_sum % k != 0:
            sorted_comb = sorted(list(comb))
            if sorted_comb not in nonDivisibles:
                print(list(comb), sorted_comb, comb_sum, comb_sum % k)
                nonDivisibles.append(sorted_comb)
    return len(nonDivisibles)


def nonDivisibleSubset(k, arr):
    length = len(arr)
    remainders = [0] * k
    for value in arr:
        remainders[value % k] += 1
    # print(remainders)
    result = 0
    for a in range(1, (k + 1) // 2):
        result += max(remainders[a], remainders[k - a])
    # print(result)
    if k % 2 == 0 and remainders[k // 2]:
        result += 1
    if remainders[0]:
        result += 1
    return result


print(nonDivisibleSubset(7, [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436 ]))
