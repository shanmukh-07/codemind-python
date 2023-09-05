n = int(input())
arr = list(map(int,input().split()))
l = []
for i in range(n):
    for j in range(i+1,n):
        if arr[i] < arr[j]:
            l.append(j-i)
            break
    else:
        l.append(0)
print(*l)