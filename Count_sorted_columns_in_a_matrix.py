r,c = map(int,input().split())
m = []
c = 0
for i in range(r):
    x = list(map(int,input().split()))
    m.append(x)
p = list(zip(*m))
for i in p:
    z = list(i)
    if sorted(z) == z:
        c+=1
print(c)