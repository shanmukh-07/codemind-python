s=input()
a,e,i,o,u=0,0,0,0,0
for v in s:
    if v=='a':
        a+=1
    if v=='e':
        e+=1
    if v=='i':
        i+=1
    if v=='o':
        o+=1
    if v=='u':
        u+=1
if a!=0 and e!=0 and i!=0 and o!=0 and u!=0:
    print(True)
else:
    print(False)
        
    