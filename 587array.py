n,k = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]
k = k%n
L2 = L[k:] + L[:k]
print(*L2,end='')
