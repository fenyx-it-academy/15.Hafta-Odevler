# https://www.hackerrank.com/challenges/library-fine/problem
# L= [8, 8, 2018]
# D= [6, 6, 2015]
# fine = [10000, 500, 15]
# L.reverse()
# D.reverse()
L = list(map(int,input().rstrip().split()))
L.reverse()
D = (list(map(int,input().rstrip().split())))
D.reverse()
fine = [10000, 500, 15]

d=0
finetotal=[0]
while d<3:
    if L[d] < D[d]:
        break
    finetotal+=[(L[d] - D[d]) * fine[d]]
    d += 1
print(max(finetotal))