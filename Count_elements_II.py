m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
d=set(a)
e=set(b)
c=[]
for i in d:
    if i not in e:
        c.append(i)
for j in e:
    if j not in d:
        c.append(j)
c=set(c)
print(len(c))