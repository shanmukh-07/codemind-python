n = input()
l = []
for i in n:
    if i.isdigit() and i not in l:
        l.append(i)
a = sorted(l,reverse = True)
c = 0
for i in range(len(a)-1,-1,-1):
    if int(a[i])%2 == 0:
        c = a.pop(i)
        break
if c == 0:
    print(-1)
else:
    a.append(c)
    b = ''.join(a)
    print(int(b))