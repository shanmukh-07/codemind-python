n = int(input())
arr = list(map(int,input().split()))
l = []
for i in range(n):
    for j in range(i,n):
        a = arr[i:j+1]
        l.append(sum(a))
print(max(l))