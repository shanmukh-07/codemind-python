def pal(a):
    r=0
    while a:
        m=a%10
        a=a//10
        r=r*10+m
    return r
l=int(input())
b=list(map(int,input().split()))
c=0
for i in b:
    if pal(i)==i:
        c+=1
print(c)