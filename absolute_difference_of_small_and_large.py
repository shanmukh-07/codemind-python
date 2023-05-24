n = input()
a = n.split()
d = []
for i in a:
    b = min(i)
    c = max(i)
    e = ord(b)
    f = ord(c)
    g = abs(e-f)
    d.append(g)
for i in d:
    print(i,end = ' ')