def fun(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

n = int(input())
a = n+1
b = n-1
while 1:
    if fun(n):
        print(0)
        break
    if fun(a) and fun(b):
        c1 = abs(n-a)
        c2 = abs(n-b)
        print(min(c1,c2))
        break
    if fun(a):
        print(abs(n-a))
        break
    if fun(b):
        print(abs(n-b))
        break
    a+=1
    b-=1