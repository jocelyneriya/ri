n = int(input())
L1 = [int(x) for x in input().split()]
k = int(input())
L2 = [int(x) for x in input().split()]
L3 = []
for x in L2 :
    if x in L1 :
        L3.append(L1.count(x))
    else :
        L3.append('Not Present')
print(*L3,end='')
