n=int(input())
arr=list(map(int,input().split()))
k=int(input())
s=[]
for i in arr:
    if i==k:
        break
    s.append(i)
a=sum(s)
print(a+k)