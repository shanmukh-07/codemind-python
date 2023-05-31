def fun(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

n = int(input())
l = []
l1 = []
for i in range(n):
    if fun(i):
        l.append(i)
for i in l:
    if n%i == 0:
        l1.append(i)
if len(l1) == 0:
    print(-1)
else:
    print(*l1)