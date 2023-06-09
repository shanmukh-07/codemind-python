n = input()
l = []
s = 'banlo'
for i in s:
    l.append(n.count(i))
l[-1] = l[-1]//2
l[-2] = l[-2]//2
print(min(l))