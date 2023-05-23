a = input()
b = input()
c = []
d = []
e = []
f = []
m = 0
for i in a:
    if i.isalpha():
        c.append(i)
for i in b:
    if i.isalpha():
        d.append(i)
for i in c:
    i=i.lower()
    e.append(i)
for i in d:
    i = i.lower()
    f.append(i)
x = set(e)
y = set(f)
k =[]
for i in x:
    if i in y:
        k.append(i)
        m=1
l=sorted(k)
n = ''.join(l)
if m == 0:
    print('-1')
else:
    print(n)