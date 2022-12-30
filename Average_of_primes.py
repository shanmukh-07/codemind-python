n=int(input())
arr=list(map(int,input().split()))
s=[]
d=0
for i in arr:
    c=0
    for j in range(1,i):
        if i%j==0:
            c+=1
    if c==1:
        s.append(i)
a=len(s)
b=sum(s)/a
print("%.2f"%b)