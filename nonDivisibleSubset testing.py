def nonDivisibleSubset(): #BU SORUYU COZEMEDIM. 
    value=input()
    array=input()
    splited=value.split()
    S=array.split()
    n=int(splited[0])
    k=int(splited[1])
    subset=[]

    for i in range(n):
        for g in range(n):
            if g>i:
                t=int(S[i])+int(S[g])
                
                if t%k!=0:
                    print(S[i],S[g])

                elif t%k==0:
                    print("-------")
                    print(S[i],S[g])
                    print("-------")
                   
  

                   

               
  

                    
                    
                    

nonDivisibleSubset()

            
            
            
    
