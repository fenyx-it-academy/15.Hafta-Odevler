
def nonDivisibleSubset(k,s):
    sonuc = 0
    liste = [0 for i in range(k)]
    for i in s:
        a=i % k
        liste[a] += 1
    division= int((k + 1) / 2)
    for i in range(1, division):
        sonuc += max(liste[i], liste[k - i])
    if k % 2 == 0 and liste[int(k / 2)]:
        sonuc += 1
    if liste[0]:
        sonuc += 1
    print(sonuc)

#
# n, k = map(int, input().split())
# S = map(int, input().split())
#
# k=3
# s=[1,7,2,4]

k=7
# s=[278,576,496,727,410,124,338,149,209,702,282,718,771,575,436]
s=[576, 771, 496, 209, 338, 436, 149, 278, 727, 282, 124, 702, 575]
# s=[278, 496, 727, 410, 124, 209, 718, 771, 575, 576, 338, 149, 702, 282, 436]
nonDivisibleSubset(k, s)
# print(len(a))