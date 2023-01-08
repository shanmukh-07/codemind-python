n=int(input())
arr=list(map(int,input().split()))
s=[]
a=[]
c=0
for i in arr:
    if i==arr.count(i):
        s.append(i)
a=set(s)
for i in a:
    if i%1==0:
        c+=1
print(c)