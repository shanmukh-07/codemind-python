n=int(input())
arr=list(map(int,input().split()))
a=sum(arr)/len(arr)
c=0
for i in range(n):
    if arr[i]<=a:
        c+=1
print(c)