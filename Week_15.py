# Hw.-1.---------------------------------------------------------------------------------
list = []
def pageCount(n, p):
    i = 0
    while i < n + 1:
        if i == n:
            list.append([i, 0])
        else:
            list.append([i, i + 1])
        i +=2
    for i in list:
        for j in i:
            if j == n:
                indexN = list.index(i)
            if j == p:
                indexP = list.index(i)
    fromFirst = indexP
    fromLast = indexN - indexP
    if fromFirst < fromLast:
        return print(fromFirst)
    else:
        return print (fromLast)

n = int(input())

p = int(input())

pageCount(n, p)

# Hw.-2.---------------------------------------------------------------------------------

import sys

matrix_list = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
               [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
               [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
               [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
               [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
               [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
               [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
               [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]


def get_min_cost(mat: list) -> int:
    cost_list = [sys.maxsize] * len(matrix_list)
    for ref_mat in matrix_list:
        cost = 0
        for x in range(0, len(mat)):
            for y in range(0, len(mat)):
                if mat[x][y] != ref_mat[x][y]:
                    cost += abs(mat[x][y] - ref_mat[x][y])
        cost_list.append(cost)
    return min(cost_list)

s = []
for s_i in range(3):
    s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
    s.append(s_t)
print(get_min_cost(s))



# Hw.-3.---------------------------------------------------------------------------------

def climbingLeaderboard(scores, alice):
    scores = list(set(scores))
    scores.sort(reverse=True)
    # print(scores)
    ranking = []

    for i in alice:
        rank = 1
        for j in scores:
            if i < j:
                rank += 1
            if i == j:
                pass
            if i > j:
                break
        ranking.append(rank)
    for f in ranking:
        print(f)


scores_count = int(input())

scores = list(map(int, input().rstrip().split()))

alice_count = int(input())

alice = list(map(int, input().rstrip().split()))
climbingLeaderboard(scores, alice)