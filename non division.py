
#**********10**5 e kadar calisiyor******************* 
import itertools
ar=[19,10,12,10,24,25,22]
k = 4

while True:
    ikili_kombinasyon=[i for i in itertools.combinations(ar,2)]
    k_true=[i for i in ikili_kombinasyon if (i[0] + i[1]) % k == 0]
    k_false = [i for i in ikili_kombinasyon if (i[0] + i[1]) % k != 0]
    if k_true==[]:
        break
    k_true_temizle=[]
    for i in k_true:
        k_true_temizle+=[i[0], i[1]]
    kac_tane_var = list ( map ( lambda x : k_true_temizle.count ( x ) , ar ) )
    ar.remove ( ar[kac_tane_var.index ( max ( kac_tane_var ) )] )

print ( len ( ar ) )

#******** calisan cozum*****************internet cozumu ne yazik ki
S=[278, 576, 496, 727, 410 ,124, 338 ,149, 209 ,702 ,282, 718, 771, 575, 436]
k=7
n=4
def solveSubset(S , k ) :
    r = [0] * k
    for value in S :
        r[value % k] += 1
  
    result = 0
    for a in range ( 1 , (k + 1) // 2 ) :
        result += max ( r[a] , r[k - a] )
    if k % 2 == 0 and r[k // 2] :
        result += 1
    if r[0] :
        result += 1
    return result
print(solveSubset ( S , k ))
