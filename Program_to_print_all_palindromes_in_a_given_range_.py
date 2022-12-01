m=int(input())
n=int(input())
for i in range(m,n+1):
    t=i
    r=0
    while(t>0):
        R=t%10
        r=(r*10)+R
        t=t//10
    if(i==r):
        print(i,end=" ")