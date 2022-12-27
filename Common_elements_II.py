m,n=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
c=[]
for i in arr1:
    if i not in arr2:
        c.append(i)
for j in arr2:
    if j not in arr1:
        c.append(j)
for i in c:
    print(i,end=' ')