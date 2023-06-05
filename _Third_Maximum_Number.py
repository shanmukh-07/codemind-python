n = int(input())
arr = list(map(int,input().split()))
a = set(arr)
l = []
for i in a:
    l.append(i)
m = sorted(l,reverse = True)
if len(m)>=3:
    print(m[2])
else:
    print(max(l))