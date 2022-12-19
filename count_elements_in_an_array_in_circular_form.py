n=int(input())
x=list(map(int,input().split()))
c=0
if ((x[-1]%2==0 and x[1]%2!=0) or (x[-1]%2!=0 and x[1]%2==0)):
    c+=1
if ((x[-2]%2==0 and x[0]%2!=0) or (x[-2]%2!=0 and x[0]%2==0)):
    c+=1
for i in range(1,len(x)-1):
    if ((x[i-1]%2==0 and x[i+1]%2!=0) or (x[i-1]%2!=0 and x[i+1]%2==0)):
        c+=1
print(c)