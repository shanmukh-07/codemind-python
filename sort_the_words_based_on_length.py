n = input()
m = n.split()
m.sort()
m.sort(key = len)
x = ' '.join(m)
print(x)