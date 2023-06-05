n = int(input())
arr = list(map(int,input().split()))
m = int(input())
l = []
for i in range(n):
    if arr[i] == m:
        l.append(i)
if len(l) == 0:
    l.append(-1)
    l.append(-1)
elif len(l) == 1:
    l.append(l[0])
l1 = []
if len(l)>2:
    l1.append(l[0])
    l1.append(l[-1])
if len(l)>2:
    print(*l1)
else:
    print(*l)