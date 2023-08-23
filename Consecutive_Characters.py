s = input()
l,l1 = [],[]
for i in range(len(s)):
    for j in range(i,len(s)):
        a = s[i:j+1]
        if len(set(a)) == 1:
            l.append(a)
            l1.append(len(a))
b = l1.index(max(l1))
print(len(l[b]))