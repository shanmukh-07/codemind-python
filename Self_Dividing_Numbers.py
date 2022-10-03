def sdn(n1):
    t=n1
    while t:
        d=t%10
        t=t//10
        if d==0 or n1%d!=0:
            return False
    return True
        
a=int(input())
s=int(input())
for i in range(a,s+1):
    if(sdn(i)):
        print(i,end=" ")