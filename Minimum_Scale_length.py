n = int(input())
arr = list(map(int,input().split()))
a = max(arr)
l = []
for i in range(1,a+1):
    for j in arr:
        if j%i ==0:
            l.append(i)
d = {}
for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
z = []
for i,j in d.items():
    if j == n:
        z.append(i)
print(max(z))