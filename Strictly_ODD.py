n = int(input())
arr = list(map(int,input().split()))
c = 0
d = 0
for i in range(1,n,2):
    d+=1
    if arr[i]%2!=0:
        c+=1
if c == d:
    print("True")
else:
    print("False")