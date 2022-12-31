n=int(input())
x=list(map(int,input().split()))
c=[]
a=0
for i in x:
    if i>a:
        c.append(i)
        a=i
if x==c:
    print("yes")
else:
    print("no")