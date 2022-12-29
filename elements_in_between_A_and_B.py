n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
d=[]
c=0
for i in arr:
    if i>=a and i<=b:
        c=1
        d.append(i)
if c==0:
    print("-1")
else:
    for i in d:
        print(i,end=' ')