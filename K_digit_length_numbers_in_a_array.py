n,k=map(int,input().split())
c=0
l=list(map(str,input().split()))
for i in range(n):
    s=len(l[i])
    if int(l[i])<0:
        s-=1
    if s==k:
        c+=1
print(c)