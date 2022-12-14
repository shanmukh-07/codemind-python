a=list(map(str,input().split()))
c=0
for i in a:
    i=i.lower()
    if ((i[0]=='a' or i[0]=='e' or i[0]=='i' or i[0]=='o' or i[0]=='u') and (i[-1]!='a' or i[-1]!='e' or i[-1]!='i' or i[-1]!='o' or i[-1]!='u')):
        c+=1
print(c)