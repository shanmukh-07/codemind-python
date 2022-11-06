n=int(input())
x=list(map(int,input().split()))
c=0
for i in range(1,len(x)-1):
    if x[i]%2!=0 and x[i+1]%2==0 and x[i-1]%2==0:
        c+=1
print(c)