n = input()
s = ''
l1,l2 = [],[]
for i in n:
    if i in 'aeiou':
        s+='V'
    else:
        s+='C'
l = list(s)
for i in range(len(l)-1):
    if l[i] == l[i+1]:
        l1.append(i)
for i in range(len(l)):
    if i not in l1:
        l2.append(l[i])
print("".join(l2))