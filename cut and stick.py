arr=[5, 4, 4 ,2, 2 ,8]
kutu=arr[:]
depo=[]
while True:
    sil=[]
    depo += [len ( kutu )]
    for i in kutu:
        x=i-min(kutu)
        if x!=0:
           sil+=[x]
    kutu=sil[:]
    if sum(kutu)==0:
        break
    else:
        continue
for i in depo:
    print(i)
