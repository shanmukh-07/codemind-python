n = input()
s = n.split()
a = s[-1]
b = list(a)
c = min(b)
l = [] 
for i in b:
    if c.lower() == i:
        l.append(i)
if len(l) == 0:
    print(c)
else:
    print(l[0])