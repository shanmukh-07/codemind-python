n = input()
c = 0
d = 0
l = []
for i in n:
    if i.isalpha() and (i == 'U' or i=='D' or i == 'L' or i == 'R'):
        l.append(i)
for i in l:
    if i == 'U':
        c+=1
    elif i == 'D':
        c-=1
    elif i == 'L':
        d+=1
    elif i == 'R':
        d-=1
if c == 0 and d == 0:
    print("True")
else:
    print("False")