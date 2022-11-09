n=int(input())
a=0
b=1
c=0
while c<n:
    print(a,end=' ')
    t=a+b
    a=b
    b=t
    c+=1
