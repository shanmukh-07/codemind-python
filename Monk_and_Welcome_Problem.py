n = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
l = []
c = 0
for i in range(n):
    c = arr1[i] + arr2[i]
    l.append(c)
print(*l)