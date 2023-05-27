def fun(s1):
    s = list(s1)
    l = []
    for i in range(len(s)):
        if s[i].isalnum():
            l.append(s[i])
            s[i] = '#'
    l.sort()        
    for i in range(len(s)):
        if s[i] == '#':
            s[i] = l[0]
            l.pop(0)
    return s


n = input()
m = n.split()
for i in m:
    z = fun(i)
    print("".join(z),end= ' ')