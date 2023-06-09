n = int(input())
arr = list(map(int,input().split()))
d = 0
a1,a2 = 0, 0
for i in range(n):
    for j in range(i,n):
        c = arr[i:j+1]
        if c.count(0) == c.count(1):
            if len(c) > d:
                d = len(c)
                a1 = i
                a2 = j
if a1 == 0 and a2 == 0:
    print(-1)
else:
    print(a1,a2)