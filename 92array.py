n,k=map(int,input().split())
num=list(map(int,input().split()))
a=[]
for i in range(len(num)):
	if(num[i]==k):
		a.append(num[i])
if(len(a)!=0):
	print('Yes')
else:
    print('No')	
