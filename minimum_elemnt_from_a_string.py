s = input()
a = s.split()
b = a[-1]
c = list(b)
d = min(c)
l=[]
for i in c:
    if d.lower() == i:
        l.append(i)
if len(l) == 0:
    print(d)
else:
    print(l[0])