s=input()
t=c=0
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
    if c>t:
        t=c
    if char==' ':
        c=0
print(t)
        