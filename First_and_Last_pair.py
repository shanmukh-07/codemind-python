n = int(input())
arr = list(map(int,input().split()))
i = 0
j = n-1
l = []
while i<=j:
    if i==j:
        l.append(arr[i])
        l.append(0)
        break
    l.append(arr[i])
    l.append(arr[j])
    i+=1
    j-=1
print(*l)