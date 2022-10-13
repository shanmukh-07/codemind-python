x,y=map(int,input().split())
if x%2==0 and (y<x or y%2==0):
    print("YES")
else:
    print("NO")
