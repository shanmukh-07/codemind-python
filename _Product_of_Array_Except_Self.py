n = int(input())
arr = list(map(int,input().split()))
p = 1
l = []
for i in arr:
    p = p*i
for i in arr:
    j = p//i
    l.append(j)
print(*l)