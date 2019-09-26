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