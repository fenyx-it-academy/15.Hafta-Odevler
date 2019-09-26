def libraryFine():
    
    returnedDate=input()
    dueDate=input()
    splited1=returnedDate.split( )
    splited2=dueDate.split( )
    
    if int(splited1[2])>int(splited2[2]):
        print(10000)

    elif int(splited1[1])>int(splited2[1]):
        print((int(splited1[1])-int(splited2[1]))*500)

    elif int(splited1[0])>int(splited2[0]):
        print((int(splited1[0])-int(splited2[0]))*15)

    else:
        print(0)


libraryFine()        
    


    
