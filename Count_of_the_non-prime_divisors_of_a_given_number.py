def prime(n):
    cnt=0
    for j in range(1,n+1):
        if n%j==0:
            cnt+=1
    if cnt==2:
        return 0
    return 1
a=int(input())
c=0
for i in range(1,a+1):
    if a%i==0 and prime(i)!=0:
        c+=1
print(c)