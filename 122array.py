b=int(input())
a=list(map(int,input().split()))
l = len(a)&-2
a[1:l:2],a[:l:2] = a[:l:2],a[1:l:2]
print(*a)
