n = int(input())
arr = list(map(int,input().split()))
d = {}
for i in arr:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
l = list(d.values())
m = max(l)
x = []
for i in arr:
    if arr.count(i) == m:
        x.append(i)
y = set(x)
if len(y) > 1:
    print(min(y))
else:
    print(*y)