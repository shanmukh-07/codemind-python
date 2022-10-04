s=input()
c=0
for char in s:
    if char=='a':
        c+=1
    if char=='e':
        c+=1
    if char=='i':
        c+=1
    if char=='o':
        c+=1
    if char=='u':
        c+=1
    if char==' ':
        print(c,end=' ')
        c=0
print(c)