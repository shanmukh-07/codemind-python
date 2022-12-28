n=int(input())
arr=list(map(int,input().split()))
s=0
arr=set(arr)
for i in arr:
    if i%2!=0:
        s=s+i
print(s)