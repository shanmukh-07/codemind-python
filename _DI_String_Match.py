s = input()
l,nl = [],[]
for i in range(len(s)+1):
    l.append(i)
for i in range(len(s)):
    if s[i]  == 'I':
        nl.append(l[0])
        l.pop(0)
    if s[i] == 'D':
        nl.append(l[-1])
        l.pop(-1)
print(*(nl+l))