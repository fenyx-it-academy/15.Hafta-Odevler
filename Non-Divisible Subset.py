import itertools
degerler = [1,7,4,2]
liste_uzunluk = []
for c in range(len(degerler),1,-1):
    tahmin = list(itertools.combinations(degerler, c))
    for i in tahmin:

        alt_liste = list(itertools.combinations(i,2))
        for d in alt_liste:
            if (d[0]+d[1])%3==0:
                kod=False
        if kod==True:
            liste_uzunluk+=[len(i)]
            break
        kod=True

print(max(liste_uzunluk))
