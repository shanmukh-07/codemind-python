def fun(n):
    c = 0
    for i in range(1,n+1):
        if n%i == 0:
            c+=i
    return c
n = input()
a = n.split(',')
l = [int(i) for i in a]
nl = []
for i in l:
    a = fun(i)
    if a in l:
        nl.append(i)
nl = sorted(nl)
if len(nl) == 0:
    print(-1)
else:
    print(*nl)