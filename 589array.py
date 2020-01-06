n = int(input())
L = [ int(x) for x in input().split()]
k=0
for x in set(L):
    if L.count(x) == 2 : 
        k = x
        break
print(k, end='')
