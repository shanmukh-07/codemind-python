def fun(n):
    l=[]
    for i in n:
        i=i.lower()
        if i not in l:
            l.append(i)
    if len(l)==len(n):
        return True
    return False
n=input()
c=0
for i in range(len(n)):
    for j in range(i,len(n)):
        p=n[i:j+1]
        if len(p)>2:
            if fun(p):
                if len(p)>c:
                    c=len(p)
                    z=p
if c==0:
    print(-1)
else:
    print(''.join(z))