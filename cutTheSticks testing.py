n=input()      #verileri alip ayiriyorum.
arr=input()
splinted=arr.split()

for i in range(int(n)):    #ayirdigim verileri integire ceviriyorum.
    splinted[i]=int(splinted[i])
print(len(splinted)) #ilk liste sayimi yazdiriyorum

while len(splinted)!=0:  #liste sayisi 0 olmadigi surece donecek bir dongu baslatiyorum
    theMin=min(splinted) #liste elemanlarinda azalmak icin her seferinde en kucuk veriyi buluyorum
    for k in range(len(splinted)): #liste ustunde dolanip 
        splinted[k]=splinted[k]-theMin#bu en kucuk veriyi cikariyorum. 

    for l in range(splinted.count(0)): #listenin icindeki tum 0 lari cikarmak icin 
        splinted.remove(0)             #kac 0 oldugunu bulup o kadar sayida dondu kurup
                                       #listedeki tum sifirlari siliyorum
    if len(splinted)==0: #liste sayisi 0 laninda dongu kiriliyor
        break
        
    print(len(splinted)) #degilse liste sayisi basiliyor.



    
            

    
    

