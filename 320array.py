n=int(input())
num=list(map(int,input().split()))
min=sorted(num)
max=min[::-1]
a=[]
for i in range(len(num)):
    a.append(max[i])
    a.append(min[i])
print(*a[:n])
