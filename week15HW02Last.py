first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

s = list(map(int, input().rstrip().split()))


#n, k = map(int, input().split())
#S = map(int, input().split())

r = [0] * k

for value in s:
    r[value % k] += 1

result = 0
for a in range(1, (k + 1) // 2):
    result += max(r[a], r[k - a])
if k % 2 == 0 and r[k // 2]:
    result += 1
if r[0]:
    result += 1
print(result)


"""first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

s = list(map(int, input().rstrip().split()))
lisst2=set()
while len(s)>=1:
    for i in s:
        if (s[0]) == 1 and k == 1:
            lisst2.add(1)
        if (s[0] + i) % k != 0 and s[0] != i:
            #if (s[0],i) not in lisst2:
            lisst2.add((i))
            lisst2.add(s[0])
                #print((i + s[0])% k)
    s.remove(s[0])
else:
    pass
#print(len(lisst2))
r = [0] * k
print(r)
"""