n=int(input())
arr=list(map(int,input().split()))
s=[]
d=[]
c=0
for i in arr:
    if i==arr.count(i):
        s.append(i)
        c=1
for i in s:
    if i not in d:
        d.append(i)
if c==0:
    print("-1")
else:
    for i in d:
        print(i,end=' ')