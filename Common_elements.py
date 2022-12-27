m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in a:
    if i in b:
        c.append(i)
for j in b:
    if j in a:
        c.append(j)
r=[i for n, i in enumerate(c) if i not in c[:n]]
for i in r:
    print(i,end=' ')