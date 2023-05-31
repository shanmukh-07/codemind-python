def fun(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

n = int(input())
l = []
for i in range(2,n):
    for j in range(2,n):
        if fun(i) and fun(j):
            if i*j == n:
                l.append(i)
                l.append(j)
m = set(l)
if len(m)==0:
    print("-1")
else:
    print(*m)