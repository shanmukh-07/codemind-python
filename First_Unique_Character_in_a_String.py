n = input()
m = n.lower()
l = []
l1 = []
for i in m:
    if i.isalpha():
        l.append(i)
for i in range(len(l)):
    if l.count(l[i]) == 1:
        l1.append(l[i])
if len(l1) == 0:
    print(-1)
else:
    m = l1[0]
    for i in range(len(l1)):
        if l[i] == m:
            print(i)