n=int(input())
c=n
while(c!=0):
  for i in range(0,c):
    if(i==c-1):
      print(1)
    else:
      print(1,end=" ")
  c=c-1 
