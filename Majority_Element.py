n=int(input())
arr=list(map(int,input().split()))
b=0
for i in arr:
    a=arr.count(i)
    if a>b and a>n/2:
        c=i
print(c)