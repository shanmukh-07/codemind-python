n1 = input()
n2 = input()
n3 = n1.lower()
n4 = n2.lower()
l1,l2 = [],[]
c = 0
for i in n3:
    if i.isalpha():
        l1.append(i)
for i in n4:
    if i.isalpha():
        l2.append(i)
l3 = set(l1)
l4 = set(l2)
for i in l3:
    if i not in l4:
        c+=1
for i in l4:
    if i not in l3:
        c+=1
print(c)