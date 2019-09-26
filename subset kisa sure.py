import itertools
degerler = [1,7,4,2]
liste_uzunluk = []
c=len(degerler)

while c>=1:
    tahmin = list(itertools.combinations(degerler, c))
    d= len(tahmin)
    while d>=0:
        d -=1
        alt_liste = list(itertools.combinations(tahmin[d], 2))
        e = len(alt_liste)
        ara_sayi = 0
        while e>0:
            e-=1
            if (alt_liste[e][0]+alt_liste[e][1])%3!=0:
                ara_sayi+=1
            if len(alt_liste)==ara_sayi:
                break
        if len(alt_liste) == ara_sayi:
            break
    if len(alt_liste) == ara_sayi:
        print(len(tahmin[d]))
        break
    c-=1
