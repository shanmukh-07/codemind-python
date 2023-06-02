n = input()
m = n.split()
l = []
for i in m:
    j = i[::-1]
    l.append(j)
b = " ".join(l)
print(b)