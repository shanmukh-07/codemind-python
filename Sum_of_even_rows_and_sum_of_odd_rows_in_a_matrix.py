r,c = map(int,input().split())
m = []
e=[]
o=[]
for i in range(r):
    x = list(map(int,input().split()))
    m.append(x)
for i in range(r):
    if i%2==0:
        e.append(m[i])
    else:
        o.append(m[i])
a=[]
b=0
c=[]
d=0
for i in e:
    a.append(sum(i))
b=sum(a)
for i in o:
    c.append(sum(i))
d = sum(c)
print(b,d)