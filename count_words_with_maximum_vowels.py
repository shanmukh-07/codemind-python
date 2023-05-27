n = input()
m = n.split()
s = 'aeiou'
l = []
for i in m:
    c = 0
    i = i.lower()
    for j in i:
        if j in s:
            c+=1
    l.append(c)
b = max(l)
print(l.count(b))