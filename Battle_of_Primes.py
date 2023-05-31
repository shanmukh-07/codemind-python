def fun(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
    
n1 = int(input())
n2 = int(input())
n = n1+n2
a = n+1
while True:
    if fun(a):
        b = a
        break
    a+=1
print(b-n)