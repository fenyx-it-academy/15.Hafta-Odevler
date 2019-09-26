print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

def cutTheSticks(arr):
    while len(arr) != 0:                                            # listenin uzunlugu sifir olunca loop tan ciksin
        print(len(arr))                                             # listenin ilk uzunluguda ciktida olmasi gerekiyor
        rra = [i - min(arr) for i in arr if (i - min(arr)) != 0]    # en kisa stick i cikariyoruz taki sifir olana kadar
        arr = rra                                                   # bu cok onemli! enson islem yaptigimiz liste verdigimiz liste olsunki enson listeyi surekli kullanalim


n = int(input())
arr = list(map(int, input().split()))
cutTheSticks(arr)
