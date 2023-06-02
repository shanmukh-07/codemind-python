n = input()
a = input()
l = []
c = 0
for i in n:
    if i.isalpha():
        l.append(i)
for i in l:
    if i == a:
        c+=1
if c==0:
    print("-1")
else:
    print(c)