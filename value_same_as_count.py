n=int(input())
arr=list(map(int,input().split()))
s=[]
a=[]
c=0
d=0
for i in arr:
    if i==arr.count(i):
        s.append(i)
for i in s:
    if i not in a:
        a.append(i)
for i in a:
    if i%1==0:
        c+=1
print(c)