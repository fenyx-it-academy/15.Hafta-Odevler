def cutTheSticks(arr):
    result=[]
    x=min(arr)
    y=max(arr)
    if x==y:
        result.append(len(arr))
        return result
    elif x==0:
        return 0
    else:
        a=list(map(lambda b:b-x,arr))
        while len(a)>1:
            result.append(len(a))
            for j in a:
                if j<=0:
                    a=list(filter(lambda k:k>0,a))
                if len(a)>0:
                    x = min(a)
                if len(a)==1:
                    result.append(1)
                    break
            a = list(map(lambda b: b - x, a))
        return(result)
arr=[8 ,8, 14, 10, 3, 5, 14 ,12]
cutTheSticks(arr)

"""def cutTheSticks(arr):
    result=[]
    x=min(arr)
    y=max(arr)
    if x==y:
        result.append(len(arr))
        print(result)
    elif x==0:
        print(0)
    else:
        a=list(map(lambda b:b-x,arr))

        while len(a)>1:
            result.append(len(a))
            for j in a:
                if j<=0:
                    a=list(filter(lambda k:k>0,a))
                if len(a)>0:
                    x = min(a)
                if len(a)==1:
                    result.append(1)
                    break
            a = list(map(lambda b: b - x, a))
        print(result)

arr=[8 ,8, 14, 10, 3, 5, 14 ,12]
cutTheSticks(arr)
"""



