n=int(input())
arr=list(map(int,input().split()))
s=0
for i in arr:
    if i%1==0:
        s=s+i
if s%2==0:
    print("1")
else:
    print("0")