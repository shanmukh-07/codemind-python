n = int(input())
l,nl = [],[]
for i in range(2**n):
    a = bin(i)[2:]
    l.append(a)
for i in l:
    b = len(i)
    c = n - b
    d = '0'*c
    k = d+i
    nl.append(k)
for i in nl:
    print(i)