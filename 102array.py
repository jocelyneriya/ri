N=int(input())
n1=list(map(int,input().split()))
n2=sorted(n1)
if(n1==n2):
	print("yes")
else:
	print("no")
