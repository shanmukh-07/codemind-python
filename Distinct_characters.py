n = input()
m = n.lower()
l = []
d = {}
a = []
for i in m:
    if i.isalpha():
        l.append(i)
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i,j in d.items():
    if j == 1:
        a.append(i)
z = sorted(a)
c = ''.join(z)
print(c)