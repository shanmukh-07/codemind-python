s = input()
l,l1 = [],[]
ss = 'aeiou'
for i in range(len(s)):
    for j in range(i,len(s)):
        a = s[i:j+1]
        l.append(a)
for i in l:
    c = 0
    for j in i:
        if j in ss:
            c+=1
    if c == len(i):
        l1.append(len(i))
print(max(l1))