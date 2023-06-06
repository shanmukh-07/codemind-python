n = int(input())
l = []
a = 0
b = 1
l.append(a)
l.append(b)
while 1:
    if len(l) == n:
        print(*l)
        break
    else:
        c = a+b
        l.append(c)
        a = b
        b = c