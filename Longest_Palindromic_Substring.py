def pal(x):
    a=''.join(x)
    if a==a[::-1]:
        return True
    return False
n=input()
n=n.lower()
n=n.replace(' ','')
x=list(n)
s=[]
for i in range(len(x)):
    for j in range(i,len(x)):
        p=x[i:j+1]
        s.append(p)
m=0
s1=''
for i in s:
    if pal(i):
        if len(i)>m:
            m=len(i)
            s1=i
print(''.join(s1))