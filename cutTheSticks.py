def cutTheSticks(arr):
    print(len(arr))
    arr2=arr
    while True:
        arr1 = []
        if len(arr2)==1:
            break
        k=0
        arr2=sorted(arr2)
        for i in arr2:
            i-=arr2[0]
            arr1.append(i)
        while True:
            if arr1[k]==0:
                arr1.remove(arr1[k])
                if len(arr1)==0:
                    quit()
                continue
            if k<len(arr1)-1:
                k+=1
            if k+1==len(arr1):
                break
        arr2=arr1
        print(len(arr1))

n = int(input())
arr = list(map(int, input().rstrip().split()))
result = cutTheSticks(arr)