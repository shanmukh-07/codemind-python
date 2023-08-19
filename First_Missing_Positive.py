n = int(input())
arr = list(map(int,input().split()))
l = sorted(arr)
m = max(l)
nl = []
for i in range(1,m+2):
    if i not in l:
        nl.append(i)
print(nl[0])