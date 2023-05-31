n=int(input())
x=list(map(int,input().split()))
c=0
c1=0
for i in range(1,len(x)-1):
    if (x[i]>x[i-1] and x[i]>x[i+1]) or (x[i]<x[i-1] and x[i]<x[i+1]):
        c+=1
if (x[0]>x[1] or x[0]<x[1]) and (x[-1]>x[-2] or x[-1]<x[-2]):
    c+=2
if c==len(x):
    n=n-1
    if n%2==0:
        print(n//2)
    else:
        n=n-1
        print(n//2)
else:
    print(-1)