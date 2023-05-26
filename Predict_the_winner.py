n = int(input())
arr = list(map(int,input().split()))
m = n//2
x = 0
y = 0
for i in range(m):
    x += arr[i]
for i in range(m,n):
    y += arr[i]
c = abs(x-y)
if c%4 == 0:
    print("X")
else:
    print("Y")