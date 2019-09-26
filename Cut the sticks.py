cubuk = [1, 2, 3, 4, 3, 3, 2, 1]
while cubuk!=[]:
    print(len(cubuk))
    cubuk = list(map(lambda x:x-min(cubuk),cubuk))
    for i in range(cubuk.count(0)): cubuk.remove(0)

# Farkli cozumler

# def solve():
#     nSticks = int(raw_input())
#     stickLengths = [int(x) for x in raw_input().split()]
#     cuts = 0
#     totalCutLength = 0
#     stickLengths = sorted(stickLengths)
#     i = 0
#     while i < len(stickLengths):
#         print len(stickLengths)-i
#         totalCutLength = stickLengths[i]
#         while i < len(stickLengths) and stickLengths[i] <= totalCutLength:
#             i += 1
#
# solve()


# import collections, sys
#
# if __name__ == '__main__':
#     N = int(sys.stdin.readline())
#     a = sorted(map(int, sys.stdin.readline().split()))
#
#     c = collections.Counter(a)
#     count = [c[k] for k in sorted(c)]
#
#     for i in range(len(count)):
#         print(sum(count[i:]))