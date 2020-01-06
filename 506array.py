a,b = list(map(int,input().split()))
c = []
for i in range(a) :
    d = list(map(int,input().split()))
    c.extend(d)

c.sort()
sum=0
for i in range(a) :
    d = []
    for j in range(b) :
        d.append(c[sum])
        sum += 1
    print(*d)
