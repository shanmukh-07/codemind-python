n=int(input())
arr=list(map(int,input().split()))
s=[]
c=0
d=0
for i in arr:
    if i==arr.count(i):
        s.append(i)
        c=1
        a=set(s)
        x=min(a)
        y=max(a)
if c==0:
    print("-1")
else:
    print(x,y)