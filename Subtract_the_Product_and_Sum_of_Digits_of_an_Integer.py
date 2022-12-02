n=int(input())
s=0
p=1
while n:
    s+=n%10
    p*=n%10
    n//=10
print(p-s)