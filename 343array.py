n = int(input())
L2 = []
for i in range(n) :
    L = [int(x) for x in input().split()]
    L2.extend(L)
L2.sort()
print(*L2,end='')
