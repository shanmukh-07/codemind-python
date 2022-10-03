n=int(input())
t=0
l=list(map(str,input().split()))
for i in range(n):
    s=len(l[i])
    if int(l[i])<0:
        s-=1
    if s>t:
        t=s
for i in range(n):
    s=len(l[i])
    if int(l[i])<0:
        s-=1
    if s==t:
        print(int(l[i]),end=' ')