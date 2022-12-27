m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
d=set(a)
e=set(b)
c=0
for i in d:
    if i in e:
        c+=1
print(c)     