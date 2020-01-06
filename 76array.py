n = int(input())
m = list(map(int,input().split()))
for x in set(m) :
    if m.count(x)==1 :
        temp = x
        break
print(temp,end='')
