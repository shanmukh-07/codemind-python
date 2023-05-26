n = input()
s = n.split()
l1 = [] 
l2 = []
m1 = []
m2 = []
for i in s:
    a = min(i)
    b = max(i)
    l1.append(a)
    l2.append(b)
for i in l1:
    c = ord(i)
    m1.append(c)
for i in l2:
    d = ord(i)
    m2.append(d)
print(abs(sum(m1)-sum(m2)))