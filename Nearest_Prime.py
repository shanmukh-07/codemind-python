def fun(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

for _ in range(int(input())):
    x = int(input())
    a = x+1
    b = x-1
    while 1:
        if fun(x):
            print(x)
            break
        if fun(a) and fun(b):
            print(min(a,b))
            break
        if fun(a):
            print(a)
            break
        if fun(b):
            print(b)
            break
        a+=1
        b-=1