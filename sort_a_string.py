n = input()
m = list(n)
l = []
for i in range(len(m)):
    if m[i].isalnum():
        l.append(m[i])
        m[i] = '#'
l.sort()
for i in range(len(m)):
    if m[i] == '#':
        m[i] = l[0]
        l.pop(0)
print("".join(m))