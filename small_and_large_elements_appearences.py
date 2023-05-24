n = input()
a = []
for i in n:
    if i.isalpha():
        a.append(i)
b = min(a)
c = max(a)
d = a.count(b)
e = a.count(c)
print(b,d,c,e)