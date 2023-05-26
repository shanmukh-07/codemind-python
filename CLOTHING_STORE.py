n = int(input())
arr = list(map(int,input().split()))
arr1 = sorted(arr)
d = {}
for i in arr1:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
c = 0
for i,j in d.items():
    if j>1:
        c += j//2
print(c)