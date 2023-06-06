n = int(input())
a = 0
b = 1
l = []
l.append(a)
l.append(b)
while 1:
    if len(l) == n:
        break
    else:
        c = a+b
        l.append(c)
        a = b
        b = c
l1,l2 = [],[]
for i in l:
    if i == n:
        print(i)
        break
    elif i<n:
        l1.append(i)
    elif i>n:
        l2.append(i)
c = max(l1)
d = min(l2)
e = abs(c - n)
f = abs(d - n)
if e>f:
    print(d)
elif e<f:
    print(c)
else:
    print(c,d)