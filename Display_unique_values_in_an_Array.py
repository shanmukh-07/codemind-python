n=int(input())
x=list(map(int,input().split()))
d={}
b=[]
for i in x:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i,j in d.items():
    if j==1:
        b.append(i)
if len(b)==0:
    print('-1')
else:
    for i in b:
        print(i,end=' ')