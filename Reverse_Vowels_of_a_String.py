def fun(s):
    s = list(s)
    l = 'aeiouAEIOU'
    m = []
    for i in range(len(s)):
        if s[i] in l:
            m.append(s[i])
            s[i] = '#'
    n = m[::-1]
    for i in range(len(s)):
        if s[i] == '#':
            s[i] = n[0]
            n.pop(0)
    return s
    
    
n = input()
b = fun(n)
c = "".join(b)
print(c)