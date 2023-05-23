a = input()
b = input()
c = []
d = []
e = [] 
f = []
for i in a:
    if i.isalpha():
        c.append(i)
for i in b:
    if i.isalpha():
        d.append(i)
for i in c:
    i = i.lower()
    e.append(i)
for i in d:
    i = i.lower()
    f.append(i)
x = set(e)
y = set(f)
m = []
for i in x:
    if i not in y:
        m.append(i)
for i in y:
    if i not in x:
        m.append(i)
n = sorted(m)
k = ''.join(n)
print(k)