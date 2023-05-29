n = int(input())
arr = list(map(int,input().split()))
l = []
for i in range(0,n,2):
    a = arr[i]
    b = arr[i+1]
    for j in range(b):
        l.append(a)
print(*l)