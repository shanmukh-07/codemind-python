n=int(input())
arr=list(map(int,input().split()))
k=int(input())
s=[]
c=0
for i in arr:
    if arr.count(i)==k:
        s.append(i)
        a=set(s)
        c=1
if c==0:
    print("-1")
else:
    for i in a:
        print(i,end=' ')