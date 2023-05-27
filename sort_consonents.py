def fun(s1):
    s = list(s1)
    m = []
    for i in range(len(s)):
        if s[i] not in 'aeiouAEIOU':
            m.append(s[i])
            s[i] = '#'
    m.sort()
    for i in range(len(s)):
        if s[i] == '#':
            s[i] = m[0]
            m.pop(0)
    return s
    
n = input()
m = n.split()
for i in m:
    z = fun(i)
    print("".join(z),end = ' ')