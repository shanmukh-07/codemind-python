s1=list(map(str,input().split()))
s2=list(map(str,input().split()))
a=[]
b=[]
c=0
for i in s1:
    i=i.lower()
    a.append(i)
for i in s2:
    i=i.lower()
    b.append(i)
for i in a:
    if i in b:
        c+=1
print(c)