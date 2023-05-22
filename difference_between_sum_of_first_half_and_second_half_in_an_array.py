n = int(input())
arr = list(map(int,input().split()))
c = n//2
s=0
m=0
for i in range(c):
    s+=arr[i]
for i in range(c,n):
    m+=arr[i]
print(abs(s-m))