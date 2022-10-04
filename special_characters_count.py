s=input()
u=0
for c in s:
    if(c.isupper() or c.islower() or c.isdigit() or c==' '):
        continue
    u+=1
print(u)