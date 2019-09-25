def nonDivisibleSubset():    
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    t = list(map(int, input().rstrip().split()))
    liste=[0]*k
    for i in t:    
        if liste[i%k]>0 and (i%k)*2==k:        
            pass
        else:
            liste[i%k]+=1
    s=len(liste)
    top=min(1,liste[0])
    if s%2==0:
        top+=liste[s//2]
        for i in range(1,s//2):        
            top+=max(liste[i],liste[-i])        
    else:
        for i in range(1,s//2+1):
            top += max(liste[i], liste[-i])        
    print(top)
result = nonDivisibleSubset()