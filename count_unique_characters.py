n = input()
a = n.lower()
l = []
d = {}
b = []
for i in a:
    if i.isalpha():
        l.append(i)
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i,j in d.items():
    if j == 1:
        b.append(i)
print(len(b))