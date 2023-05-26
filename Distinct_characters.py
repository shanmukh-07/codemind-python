n = input()
m = n.lower()
l1 = []
for i in m:
    if i.isalpha():
        l1.append(i)
l2 = set(l1)
c = sorted(l2)
d = ''.join(c)
print(d)