n = int(input())
arr = list(map(int,input().split()))
c = n//2
e=0
f=0
for i in range(c):
    e+=arr[i]
print(e)
for i in range(c,n):
    f+=arr[i]
print(f)