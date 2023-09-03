n = input()
l = n.split(',')
nl = []
for i in l:
    c = i.split(':')
    nl.append(c)
s = ''
for i in nl:
    a = len(i[0])
    b = list(i[1])
    cl = []
    for j in b:
        if int(j) <= a:
            cl.append(int(j))
    if len(cl) == 0:
        s+='X'
    else:
        s+=i[0][max(cl)-1]
print(s)