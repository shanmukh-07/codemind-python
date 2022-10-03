n=int(input())
c=0
l=list(map(str,input().split()))
for i in range(n):
    s=len(l[i])
    if int(l[i])<0:
        s-=1
    print(s,end=' ')