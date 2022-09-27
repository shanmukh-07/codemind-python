n=int(input())
r=0
while n>0:
    R=n%10
    r=(r*10)+R
    n=n//10
print(r)