n = int(input())
l,l1 = [],[]
for i in range(1,n+1):
    c = 2**i
    l.append(c)
for i in l:
    d = abs(i-n)
    l1.append(d)
print(min(l1))