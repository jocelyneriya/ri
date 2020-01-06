n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in range(0,len(l)):
  if(l[i] not in l1):
    l1.append(l[i])
  else:
    l2.append(l[i])
for i in range(0,len(l1)):
  if(l1[i] not in l2):
    print(l1[i])
