t=int(input())
for i in range(t):
    l,r=map(int,input().split())
    count=0
    for i in range(l,r+1):
        k=i%10
        if k==2 or k==3 or k==9:
            count=count+1
    print(count)
        
        
        
