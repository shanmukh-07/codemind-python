s=input()
l=set(s)
c=[]
for i in l:
    c.append(s.count(i))
if c[-2]!=c[-3]:
    print('Not Valid')
else:
    print('Valid String')