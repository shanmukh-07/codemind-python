n,t = map(int,input().split())
arr = list(map(int,input().split()))
l = []
for i in range(n):
    for j in range(i,n):
        c = arr[i:j+1]
        l.append(c)
d = 0
for i in l:
    z = sum(i)
    if z == t:
        d+=1
print(d)