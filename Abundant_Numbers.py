n=int(input())
sum=1  
for i in range(1,n):
  if(n%i==0):
      sum=sum+i
if(sum>n):
    print("True")
else:
  print("False")