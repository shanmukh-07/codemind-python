def fun(z):
    a = z[0]
    b = z[1]
    for i in range(2,len(z)):
        if z[i] == a+b:
            a = b
            b = z[i]
        else:
            return False
    return True
    
n = int(input())
arr = list(map(int,input().split()))
if len(arr)<=2:
    print("no")
elif fun(arr):
    print("yes")
else:
    print("no")