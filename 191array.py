s1,s2=map(str,input().split())
f=1
t1=list(set(s1))
t2=list(set(s2))
for i in range(len(t1)):
    if(t1[i] not in t2):
        f=0
        break 
for j in range(len(t2)):
    if(t2[i] not in t1):
        f=0
        break 
if(f==1):
