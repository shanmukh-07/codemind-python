a=int(input())
b=a*a
sum=0
while(b>0):
    p=b%10
    sum=sum+p
    b=b//10
if(sum==a):
    print("Neon Number")
else:
    print("Not Neon Number")