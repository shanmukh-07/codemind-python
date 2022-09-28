n=int(input())
sum=0
prod=1
while n>0:
    p=n%10
    sum=sum+p
    prod=prod*p
    n=n//10
if sum==prod:
    print("Spy Number")
else:
    print("Not Spy Number")