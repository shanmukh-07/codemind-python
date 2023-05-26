def prime(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True
n = int(input())
arr = list(map(int,input().split()))
for i in arr:
    if i == 1 or i<0:
        arr.remove(i)
p,np = 1,1
for i in arr:
    if prime(i):
        p*=i
    else:
        np*=i
print(abs(p-np))