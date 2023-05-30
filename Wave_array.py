n = int(input())
x = list(map(int,input().split()))
c = 0
for i in range(1,n-1):
    if (x[i-1] > x[i] and x[i] < x[i+1]) or (x[i-1] < x[i] and x[i] > x[i+1]):
        c+=1
if (x[0] > x[1] or x[0] < x[1]) and (x[-1] > x[-2] or x[-1] < x[-2]):
    c+=2
if n==c:
    print("yes")
else:
    print("no")