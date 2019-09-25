#Library Fine

tarih1=list(map(int,input().split()))       #returned date
tarih2=list(map(int,input().split()))       #due date

if tarih1[2]>tarih2[2]:   #yil buyukse
    print("10000")
elif tarih1[2]<tarih2[2]:   #teslim edilmesi gereken tarihin yilindan daha erken bi yilda teslim
    print(0)
elif tarih1[1]>tarih2[1]:       #ay gecmisse
    print(500*(tarih1[1]-tarih2[1]))
elif tarih1[1]<tarih2[1]:       #teslim edilmesi gereken tarihin ayindan daha erken bi ayda teslim
    print(0)
elif tarih1[0]>tarih2[0]:         #gun gecmisse
    print(15*(tarih1[0]-tarih2[0]))
else:
    print(0)

#Cut the sticks

n = int(input())
arr = list(map(int, input().rstrip().split()))

while len(arr)>0:
    print(len(arr))
    liste=[i-min(arr) for i in arr if (i-min(arr))>0]
    arr=liste[:]

#nonDivisibleSubset
arr1=list(map(int,input().strip().split()))
arr2=list(map(int,input().strip().split()))
def nonDivisible(k,arr):
    f = [0]*k
    res=0
    for i in range(len(arr)):
        f[arr[i] % k] += 1
    if (k% 2 == 0) and f[k/ 2]:
        res +=1
    if f[0]:
        res +=1
    for i in range(1, (k // 2) + 1):
        res += max(f[i], f[k - i])
    return res

print(nonDivisible(arr1[1], arr2))
