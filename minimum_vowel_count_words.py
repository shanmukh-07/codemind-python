m = input()
n = m.split()
s = 'aeiou'
l = []
for i in n:
    c = 0
    i = i.lower()
    for j in i:
        if j in s:
            c+=1
    l.append(c)
print(l.count(min(l)))