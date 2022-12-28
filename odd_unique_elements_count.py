n=int(input())
arr=list(map(int,input().split()))
c=0
arr=set(arr)
for i in arr:
    if i%2!=0:
        c+=1
print(c)