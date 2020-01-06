n = int(input())
L = [ int(x) for x in input().split()]
L.sort()
res = L[0] + L[1]
print(res, end='')
