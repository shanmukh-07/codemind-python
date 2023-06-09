n = input()
m = n.split()
l,l1 = [],[]
for i in m:
    j = list(i)
    l.append(j)
for i in l:
    if i[0] in 'aeiouAEIOU':
        i.append('ma')
    else:
        c = i[0]
        i.remove(c)
        i.append(c)
        i.append('ma')
    l1.append(i)
for i in range(len(l1)):
    l1[i].append('a'*(i+1))
for i in l1:
    m =''.join(i)
    print(m,end = ' ')