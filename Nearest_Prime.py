def fun(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    a = n+1
    b = n-1
    while 1:
        if fun(a) and fun(b):
            print(min(a,b))
            break
        elif fun(a):
            print(a)
            break
        elif fun(b):
            print(b)
            break
        elif fun(n):
            print(n)
            break
        else:
            a+=1
            b-=1