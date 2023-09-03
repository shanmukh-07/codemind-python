n = input()
d = {}
for i in n:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
l = []
for i in d.values():
    l.append(i)
s = set(l)
nl = [i for i in s]
m = sorted(nl,reverse = True)
if len(m)<2:
    print(-1)
else:
    z = []
    for i,j in d.items():
        if j == m[1]:
            z.append(i)
    print(z[0])