n = int(input())
arr = list(map(str,input().split()))
l = []
for i in arr:
    i = i[::-1]
    l.append(int(i))
print(*l)