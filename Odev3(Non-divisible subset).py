s=[1,7,2,4,5]
k=3
s=set(s)                            # verilen liste kumeye cevrildi ayni sayilardan kurtulmak icin.
kalanlar=[i%k for i in s]           # kalanlar listesine her sayinin k ile bolumunden kalan atandi.
liste=[0]*k                         # bu liste k ile bolumden kac tane kalan olabilirse o kadar sifir tutacak.
sayac=0
for i in kalanlar:                  # bu dongu her kalanin kac tane oldugunu bulmak icin kullanildi.
    liste[i] += 1
for i in range(k//2+1):             # kalalari birbiriyle eslestirecegimizden k nin yarisi kadar for'u dondurduk.
    if i==0 or k%2==0 and i == k//2:  # burda k ile tam bolunenler ve k cift sayi ise listenin orta elemani kendi ile
        if liste[i]>0:                # eslestiginden ve deger 0 degil ise sayaci sadece 1 artiracagiz.
            sayac+=1
    else:                             # diger eslesmelerde yuksek olan sayiyi alacagiz.
        sayac += max(liste[i], liste[k - i])
print(sayac)