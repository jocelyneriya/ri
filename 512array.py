n = int(input())
L = input().split()
L2 = []
for i in range(n) :
    i2 = i*2
    L2.append((L[i2],int(L[i2+1])))
L2.sort(key = lambda x : x[1])
L3 = []
for x in L2 :
    L3.append(x[0])
print(*L3,sep='\n',end='')
