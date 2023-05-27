n = input()
m = n.split()
l = []
for i in m:
    i = i.lower()
    z = list(i)
    l.append(set(z))
b = l[0]
for i in range(0,len(l)):
    b = b.intersection(l[i])
if len(b) == 0:
    print('-1')
else:
    print(min(b))