n = int(input())
arr = list(map(int,input().split()))
t = int(input())
l = []
for i in range(n):
    if arr[i] == t:
        l.append(i)
if len(l) == 0:
    print(-1)
else:
    print(*l)