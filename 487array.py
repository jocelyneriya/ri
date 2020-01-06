n=int(input())
l=list(map(int,input().split()))
r=[]
t=list(set(l))
for i in range(0,len(t)):
 c=0
 for j in range(0,len(l)):
  if(t[i]==l[j]):
   c=c+1
 r.append(c) 
c=0
for i in range(0,len(r)):
 if(r[i]==3):
  c=c+1
print(c)
