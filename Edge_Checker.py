x,y=map(int,input().split())
if x-y==1 or y-x==1 or x-y==9 or y-x==9:
    print("Yes")
else:
    print("No")