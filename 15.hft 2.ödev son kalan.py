
k=18
s=[18,1,3,36,54,180]

#n listesindeki tüm ikililerin k ya tam bölünüp bölünmediğini kontorl ediyorim


##mod k ya göre 0 olanların hepsini çıkarırım
##çünkü onlardan bir tane olması yeterli 


def nonDivisibleSubset(k, s):
    sonuc=0
    if k == 1:
        return 1
    m=[]
    for i in range(len(s)):
        m += [s[i]%k]
    kume=set(m)
    kalanlar=list(kume)
    kalanlar.sort()
    if 0 in kalanlar:
        sonuc+=1
        kalanlar.remove(0)
    if k%2==0:
        if int(k/2) in kalanlar:
            sonuc+=1
            kalanlar.remove(k/2)
    for i in kalanlar:
        if k-i in kalanlar:
            sonuc+=(max(m.count(i),m.count(k-i)))/2
        else:
            sonuc+= m.count(i)
    return int(sonuc)
print(nonDivisibleSubset(k,s))


                

    


    
        

