a,b = map(int,input().split())
m = str(a)
c = list(m)
l,l1 = [],[]
for i in range(b):
    l.append(c[i])
k = "".join(l)
k = int(k)

z = m[::-1]
y = list(z)
for i in range(b):
    l1.append(y[i])
x = "".join(l1)
w = x[::-1]
w = int(w)
print(abs(k-w))